from django.shortcuts import render
from .models import Customer
from .models import Order
from .models import Product

# Create your views here.


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
    'customers':customers,
    'orders':orders,
    'total_orders':total_orders,
    'delivered':delivered,
    'pending':pending
    }

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all().order_by('name')

    return render(request, 'accounts/products.html', {'products':products})


def customers(request):
    return render(request, 'accounts/customers.html')
