from django.shortcuts import render
from .models import Customer


def show_cards(request):
    customers = Customer.objects.all()
    for customer in customers:
        
        customers_descriptions = {
            'name': customer.full_name,
            'phone_number': customer.phone_number
        }
    return render(request, "customers.html", context={'customers': customers_descriptions})


def index(request):
    return render(request, "index.html")
