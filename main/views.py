import asyncio
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from config import settings
from telegram_files.telegram_utils import send_telegram_message
from .models import Info, Portfolio, Reviews, Services, ContactUsModel, IpAddress
from rest_framework import generics, viewsets, status
from .serializers import InfoSerializer, PortfolioSerializer, ReviewsSerializer, ServicesSerializer, \
    ContactUsSerializer, LikeSerializer


class MainPageAPIView(generics.ListAPIView):
    permission_classes = []
    serializer_class = InfoSerializer
    queryset = Info.objects.all()


class PortfolioViewSet(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class PortfolioDetailView(generics.RetrieveAPIView):
    serializer_class = PortfolioSerializer
    lookup_field = 'id'

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_queryset(self):
        return Portfolio.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        ip = self.get_client_ip(request)

        if IpAddress.objects.filter(ip=ip).exists():
            instance.views.add(IpAddress.objects.get(ip=ip))
        else:
            ip_instance = IpAddress.objects.create(ip=ip)
            instance.views.add(ip_instance)

        serializer = PortfolioSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewsAPIView(generics.ListAPIView):
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all().order_by('-created_at')


class ServicesAPIView(generics.ListAPIView):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUsModel.objects.all()
    serializer_class = ContactUsSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        bot_token = settings.TELEGRAM_BOT_TOKEN
        admin_chat_id = settings.TELEGRAM_CHAT_ID
        message = (
            f"You have a new message from Viento:\n\n"
            f"Name: {instance.name}\n"
            f"Phone: {instance.phone_number}\n"
            f"Message: {instance.message}"
        )

        asyncio.run(send_telegram_message(bot_token, admin_chat_id, message))


class CreateLikeView(APIView):
    def get(self, request, id):
        try:
            portfolio = Portfolio.objects.get(id=id)
        except Portfolio.DoesNotExist:
            return Response({'error': 'Portfolio not found'}, status=status.HTTP_404_NOT_FOUND)

        likes_count = portfolio.likes_count
        return Response({'likes_count': likes_count}, status=status.HTTP_200_OK)

    def post(self, request, id):
        try:
            portfolio = Portfolio.objects.get(id=id)
        except Portfolio.DoesNotExist:
            return Response({'error': 'Portfolio not found'}, status=status.HTTP_404_NOT_FOUND)

        like_data = {
            'portfolio': portfolio.id,
            'ip_address': request.META['REMOTE_ADDR']
        }

        serializer = LikeSerializer(data=like_data)
        if serializer.is_valid():
            serializer.save()

            portfolio.likes_count += 1
            portfolio.save()

            data = {
                'status': 'Like successfully added',
                'Portfolio': portfolio.name,
                'ip-address': serializer.data['ip_address'],
                'likes_count': portfolio.likes_count
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
