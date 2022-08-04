import os
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import Product
from django.contrib import messages
from django.db.models import Q

@staff_member_required
@login_required(login_url='user_login')
@never_cache
def admin_site(request):
    user_dict={
        'user_list':User.objects.all()
    }
    return render(request,'superuserhome.html',user_dict)

@login_required(login_url='user_login')
def user_delete(request,id):
    instence_user=User.objects.get(id=id)
    instence_user.delete()
    return redirect(admin_site)

@login_required(login_url='user_login')
def user_edit(request,id):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        username=request.POST['username']
        staffstrue = request.POST.get('staffstrue', False)
        superuseractive = request.POST.get('superuseractive', False)
        user_detail=User.objects.get(id=id)
        if user_detail.email != email:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email is already taken')
                return HttpResponse("<script>window.history.back()</script>")
            else:
                user=User.objects.get(id=id)
                user.email=email
                user.first_name=fname
                user.last_name=lname
                user.username=username
                if staffstrue == 'True' :
                    user.is_staff=True
                else:
                    user.is_staff=False
                if superuseractive == 'True' :
                    user.is_superuser=True 
                else:
                    user.is_superuser=False
                user.save()
                return redirect(admin_site)
        else:
            user=User.objects.get(id=id)
            user.first_name=fname
            user.last_name=lname
            user.username=username
            if staffstrue == 'True':
                user.is_staff=True
            else:
                user.is_staff=False
            if superuseractive == 'True':
                    user.is_superuser=True 
            else:
                    user.is_superuser=False
            user.save()
            return redirect(admin_site)
    user_dict={
        'user_list':User.objects.get(id=id)
    }
    return render(request,'useredit.html',user_dict)

@login_required(login_url='user_login')
def user_add(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        staffstrue = request.POST.get('staffstrue', False)
        superuseractive = request.POST.get('superuseractive', False)
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Name is already taken')
                return HttpResponse("<script>window.history.back()</script>")    
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is already taken')
                return HttpResponse("<script>window.history.back()</script>")
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=fname,last_name=lname)
                if staffstrue == 'True' :
                    user.is_staff=True
                if superuseractive == 'True' :
                    user.is_superuser=True                    
                user.save()
        else:
            messages.info(request,'Password not matching....')
            return HttpResponse("<script>window.history.back()</script>")
        return redirect(admin_site)
    return render(request,'user_creation.html')

@login_required(login_url='user_login')
def search_user(request):
    search = request.POST['search']
    search_dict={
        'search_data':User.objects.filter(Q(username__icontains=search) | Q(email__icontains=search) | Q(first_name__icontains=search) | Q(last_name__icontains=search) )
    }
    return render(request,'superuserhome.html',search_dict)

@login_required(login_url='user_login')
def product_deatails(request):
    dict_product={
        'product': Product.objects.all()
    }
    return render(request,'productdeatil.html',dict_product)

@login_required(login_url='user_login')
def add_product(request):
    if request.method == 'POST':
        name=request.POST['name']
        price=request.POST['price']
        count=request.POST['count']
        description=request.POST['description']
        product=Product()
        if len(request.FILES) != 0:
            try:
                image=request.FILES['image']
                product.image=image
            except:
                pass
        product.name=name
        product.price=price
        product.count=count
        product.description=description
        product.save()
        return redirect(add_product)
    return render(request,'addproduct.html')

def edit_product(request,id):
    if request.method == 'POST':
        name=request.POST['name']
        price=request.POST['price']
        count=request.POST['count']
        description=request.POST['description'] 
        product=Product.objects.get(id=id)   
        if len(request.FILES) != 0:
            try:
                image=request.FILES['image']
                product.image=image
                image_path=product.image.path
                os.remove(image_path)
            except:
                pass   
        product.name=name
        product.price=price
        product.count=count
        product.description=description
        product.save()  
        return redirect(product_deatails)      

    dict_product={
        'product': Product.objects.get(id=id)
    }
    return render(request,'editproduct.html',dict_product)