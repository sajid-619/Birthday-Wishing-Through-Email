from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Customer
from .serializers import CustomerSerializer

class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    data = {
        'name': customer.name,
        'email': customer.email,
        'birthday': customer.birthday.strftime('%Y-%m-%d')
        # Add more fields as needed
    }
    return JsonResponse(data)
