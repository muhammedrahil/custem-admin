
from . import views
from django.urls import path 

urlpatterns = [
    path('',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('registration',views.registration,name='registration'),
    

]