from django.contrib import admin
from .models import Customer
from .models import Order
from .models import Product

# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
