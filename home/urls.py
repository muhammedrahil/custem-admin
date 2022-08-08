
from . import views
from django.urls import path 

urlpatterns = [
    path('',views.home,name='home'),
    path('cart_section/<int:id>',views.cart_section,name='cart_section'),
    path('cart',views.cart,name='cart'),
]