from rest_framework import serializers
from config import settings
from .models import Info, Portfolio, PortfolioScreenshots, PortfolioDoneThings, Reviews, Services, ContactUsModel, Like
from telegram_files.telegram_utils import send_telegram_message


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('completed_projects', 'employees', 'partners', 'experience')


class PortfolioScreenshotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioScreenshots
        fields = '__all__'


class PortfolioDoneThingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioDoneThings
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    screenshots = PortfolioScreenshotsSerializer(many=True)
    done_things = PortfolioDoneThingsSerializer(many=True)
    views = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = '__all__'

    def create(self, validated_data):
        screenshots = validated_data.pop('screenshots')
        portfolio = Portfolio.objects.create(**validated_data)
        for shot in screenshots:
            Portfolio.objects.create(portfolio=portfolio, **shot)
        return portfolio

    def get_views(self, obj):
        count = obj.views.count()
        return count


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsModel
        fields = ('id', 'name', 'phone_number', 'message')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
