from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from custem_admin.models import Product
from django.db.models import Q

@login_required(login_url='user_login')
@never_cache
def home(request):
    dict_product={
        'product': Product.objects.all()
    }
    return render(request,'productList.html',dict_product)

def search_item(request):
    search=request.POST['search']
    dict_product={
        'search_product': Product.objects.filter(name__icontains=search)
    }
    return render(request,'productList.html',dict_product)