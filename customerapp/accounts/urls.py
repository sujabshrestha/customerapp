from django.urls import path,include
from .views import home,products,customer,createorder,updateorder,deleteorder
urlpatterns = [
    path('', home,name='home'),
    path('products/', products,name='products'),
    path('customer/<int:pk>/', customer,name='customer'),
    path('createorder/', createorder,name='createorder'),
    path('updateorder/<str:pk>', updateorder,name='updateorder'),
    path('deleteorder/<str:pk>', deleteorder,name='deleteorder'),
 
]
