from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from custem_admin.models import Product
from django.contrib import messages

@login_required(login_url='user_login')
@never_cache
def home(request):
    if request.method == 'POST':
        search=request.POST['search']
        dict_search_product={
            'product': Product.objects.filter(name__icontains=search)
        }
        return render(request,'productList.html',dict_search_product)
    dict_product={
        'product': Product.objects.all()
    }
    return render(request,'productList.html',dict_product)

def cart_section(request,id):
    id=id
    add_cart_product=Product.objects.get(id=id)
    if request.method == "POST":
        add_cart_product.is_cart=False
        add_cart_product.save()
        messages.info(request, 'Product Remove to cart successfully!')
        return redirect(cart)
    add_cart_product.is_cart=True
    add_cart_product.save()
    messages.info(request, 'Product Add to cart successfully!')
    return redirect(home)


@login_required(login_url='user_login')
def cart(request):
    if request.method == 'POST':
        search=request.POST['search']
        dict_search_product={
            'product': Product.objects.filter(name__icontains=search , is_cart=True)
        }
        return render(request,'productList.html',dict_search_product)
    dict_product={
        'product': Product.objects.filter(is_cart=True)
    }
    return render(request,'cart.html',dict_product)
    
