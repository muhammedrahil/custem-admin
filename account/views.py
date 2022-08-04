from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from home.views import home
from custem_admin.views import admin_site
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def registration(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Name is already taken')
                return HttpResponse("<script>window.history.back()</script>")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is already taken')
                return HttpResponse("<script>window.history.back()</script>")
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=fname,last_name=lname)
                user.save()
        else:
            messages.info(request,'Password not matching....')
            return HttpResponse("<script>window.history.back()</script>")
        return redirect(user_login)
    return render(request,'signup.html')



@never_cache
def user_login(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect(admin_site)
        else :
            return redirect(home)
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if request.user.is_superuser:
                return redirect(admin_site)
            else :
                return redirect(home)
        else :
            messages.error(request,'Incorrect Username or Password')
            return redirect(user_login)
    return render(request,'login.html')


@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect(user_login)

