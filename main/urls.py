from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import MainPageAPIView, PortfolioViewSet, PortfolioDetailView, ReviewsAPIView, ServicesAPIView, \
    ContactUsViewSet, CreateLikeView

app_name = 'main'

router = DefaultRouter()
# router.register(r'portfolios', PortfolioViewSet, basename='portfolio'),
router.register(r'contact-us', ContactUsViewSet, basename='contact-us')


urlpatterns = [
    path('', MainPageAPIView.as_view(), name='main'),
    path('reviews/', ReviewsAPIView.as_view(), name='reviews'),
    path('services/', ServicesAPIView.as_view(), name='services'),
    path('portfolios/', PortfolioViewSet.as_view(), name='portfolios'),
    path('portfolios/<int:id>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('portfolios/<int:id>/create-like/', CreateLikeView.as_view(), name='create-like'),

]

urlpatterns += router.urls

