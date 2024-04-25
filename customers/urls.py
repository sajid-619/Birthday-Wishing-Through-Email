from django.urls import path
from .views import CustomerCreateView, customer_detail

urlpatterns = [
    path('register/', CustomerCreateView.as_view(), name='customer-register'),
    path('<int:pk>/', customer_detail, name='customer-detail'),
]
