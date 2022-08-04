
from . import views
from django.urls import path 

urlpatterns = [
    path('',views.home,name='home'),
    path('search',views.search_item,name='search_item'),
]