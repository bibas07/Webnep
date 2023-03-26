from django.shortcuts import render, redirect
from .forms import RegisterUser, ProfileForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CaptchaRegForm
# Create your views here.

def register(request):
    context={
        'title':"Register"
    }
    if request.method == "POST":
        captcha_form = CaptchaRegForm(request.POST)
        form = RegisterUser(request.POST)
        if form.is_valid() and captcha_form.is_valid():
            form.save()

            return redirect("dashboard")
    else:
        form = RegisterUser()
        captcha_form = CaptchaRegForm()                        
    context["form"] = form
    context["captcha_form"] = captcha_form
    return render(request, "content/register.html", context)

def profileView(request):
    context = {
        'title':'Profile',
        'infos': UserProfile.objects.all().filter(user_name=request.user).last()
    }
    return render(request,"content/profile.html", context)

@login_required
def updateProfile(request):
    context = {
        'title':'Update Profile'
    }
    user = request.user
    UserProfile.objects.update(user_name=user)
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            cus = form.save(commit=False)
            cus.user_name = user
            cus.save()
            return redirect("profile")
    else:
        form = ProfileForm()
    context['form'] = form
    return render(request, "content/edit_profile.html", context)

        

