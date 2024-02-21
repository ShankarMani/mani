from django.shortcuts import render,redirect
from accounts.forms import Form
from django.contrib.auth import authenticate,login
from django.http import HttpResponse

# Create your views here.
def registration (request):
    registered = False
    if request.method == 'POST':
        form=Form(request.POST)
        
        if form.is_valid() :
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(form.errors)

    else:
        form=Form()
    
    return render(request,"registration.html",{'form':form,'registered':registered})       
    
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return redirect("Home")
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("please check ur cred's")
    return render(request,'login.html',{})
