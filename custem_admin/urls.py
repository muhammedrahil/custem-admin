from . import views
from django.urls import path 

urlpatterns = [
    path('',views.admin_site,name='admin_site'),
    path('user_delete/<int:id>',views.user_delete,name='user_delete'),
    path('user_edit/<int:id>',views.user_edit,name='user_edit'),
    path('user_add',views.user_add,name='user_add'),
    path('product_deatails',views.product_deatails,name='product_deatails'),
    path('add_product',views.add_product,name='add_product'),
    path('edit_product/<int:id>',views.edit_product,name='edit_product'),




]