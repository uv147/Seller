from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render


def handlelogin(request):
    return render(request,'login.html')
def handlesignup(request):
    return render(request,'signup.html')
def handleseller(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        brand=request.POST.get('BrandName')
        pan=request.POST.get('PAN')
        password=request.POST.get('pass1')
    
        confirmpassword=request.POST.get('pass2')
        if password!=confirmpassword:
           messages.warning(request,"Password is Incorrect")
           return redirect('/seller')
         
          
        try:
           if User.objects.get(username=uname):
                messages.info(request,'UserName is Taken')
                return redirect('/seller')
        except:
           pass
        try:
           if User.objects.get(email=email):
                messages.info(request,'Email is Taken')
                return redirect('/seller')
        except:
           pass
        try:
           if User.objects.get(BrandName=brand):
                messages.info(request,'BrandName is Taken')
                return redirect('/seller')
        except:
           pass
        try:
           if User.objects.get(PAN=pan):
                messages.info(request,'Pan is Taken')
                return redirect('/seller')
        except:
           pass
        myuser= User.objects.create_user(uname, email, password)
        myuser.save()
        
        return HttpResponse('Seller Signup Success')

    return render(request,'seller.html')
def handlesellerlogin(request):
    if request.method=='POST':
       uname=request.POST.get('username')
      
       pass1=request.POST.get('pass1')
       myuser=authenticate(username=uname,password=pass1)
       if myuser is not None:
           login(request,myuser)
           messages.success(request,'login success')
           return redirect('/')
       else:
           messages.error(request,'Invalid Credentials')
           return redirect('/sellerlogin')
           
    return render(request,'sellerlogin.html')


