from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_url_name'),
    path('products/', views.products, name='product_url_name'),
    path('customers/<str:pk_test>/', views.customers, name='customer_url_name'),
    path('create_order/<str:pk>/', views.create_order, name='create_order_url_name'),
    path('update_order/<str:pk>/', views.update_order, name='update_order_url_name'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_order_url_name'),
]
