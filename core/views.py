from django.contrib import messages
from django.contrib.auth import login, logout
from django.db.models import Q
from django.shortcuts import render, redirect
from core.forms import *
# Create your views here.
def Register(request):
    username = request.POST.get("usernameval")
    email = request.POST.get("emailval")
    password = request.POST.get("passwordval")
    confirm_password = request.POST.get("password2val")
    # type = request.POST.get("type")
    if email and password and confirm_password and username:
        if len(password) > 7 and str(password) == str(confirm_password):
            user_email = Account.objects.filter(email=email)

            if user_email:
                messages.warning(request, "Email Already Exist")
                return render(request,"register.html", {})
            else:
                user = Account.objects.create_user(username=username,email=email,password=password)
                print(user)
                login(request, user)
                messages.success(request,"Account was created for "+username)
                if request.user.user_type=="MANAGER":
                    return redirect("manager-home")
                if request.user.user_type=="INTERN":
                    return redirect("intern-home")

    return render(request,"register.html")

def Login(request):
    if request.user.is_authenticated:
        if request.user.user_type == "MANAGER":
            return redirect("manager-home")
        if request.user.user_type == "INTERN":
            return redirect("intern-home")
    username = request.POST.get("email")
    password = request.POST.get("password")
    user = Account.objects.filter(Q(email=username) | Q(username=username)).first()
    if user:
        if user.check_password(password) or user.password==password:
            login(request, user)
            messages.success(request, "user login successfully")
            if request.user.user_type == "MANAGER":
                return redirect("manager-home")
            if request.user.user_type == "INTERN":
                return redirect("intern-home")
        else:
            messages.error(request, "Invalid Password")
            return render(request,"login.html", {})
    else:
        messages.error(request, "Invalid Username and Password")
        return render(request,"login.html", {})

    return render(request,"login.html")

def Logout(request):
    logout(request)
    messages.success(request, "logout successfully")
    return redirect("login")