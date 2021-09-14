from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_url_name'),
    path('products/', views.products, name='product_url_name'),
    path('customers/<str:pk_test>/', views.customers, name='customer_url_name'),
]
