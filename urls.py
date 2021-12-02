from rest_framework.urls import path
from .views import ManufacturerAPIView, MoldingAPIView


urlpatterns = [
    path('manufacturer/', ManufacturerAPIView.as_view(), name='manufacturer'),
    path('molding/', MoldingAPIView.as_view(), name='molding'),
]
