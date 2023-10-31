from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from credentials.models import Formdatas


def homepg(request):
    return redirect('/')
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User name taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('/')
            else:
                user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                return redirect('login')
                print("User Created")

        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def details(request):
    if request.method =="POST":
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone= request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        dept = request.POST.get('dept')
        course =request.POST.get('course')
        formdet = Formdatas(name=name,dob=dob,age=age,gender=gender,phone=phone,email=email,address=address,dept=dept,course=course)
        formdet.save()
        print("Submitted")
        return redirect('/')
    return render(request,'detail.html')
