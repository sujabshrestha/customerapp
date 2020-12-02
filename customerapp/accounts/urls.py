from django.urls import path,include
from .views import home,products,customer
urlpatterns = [
    path('', home,name='home'),
    path('products/', products,name='products'),
    path('customer/<int:pk>/', customer,name='customer'),
 
]
