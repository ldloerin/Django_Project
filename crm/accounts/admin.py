from django.contrib import admin
from .models import Customer
from .models import Order
from .models import Product
from .models import Tag

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
