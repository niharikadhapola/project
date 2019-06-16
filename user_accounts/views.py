# System imports
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# User defined imports
from .models import UserProfile
from .forms import UserForm, UserProfileInfoForm

# Create your views here.

# Home page at localhost:8000
def index(request):
    return render(request,'user_accounts/index.html')

# Just for show -- Note to Prarthna : "Remove it if not needed"
@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Registering a user - Company or Individual
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'user_accounts/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

# Individual login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        x = User.objects.get(username=username)
        y = UserProfile.objects.get(user=x)
        print(y.address)
        h=y.address


        user = authenticate(username=username, password=password,)
        if user:
            if user.is_active :
                if  y.category=='Individual':
                    login(request,user)
                else:
                    return HttpResponse("not valid.")
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'user_accounts/login.html', {})


# Company Login view
def comp_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        x = User.objects.get(username=username)
        y = UserProfile.objects.get(user=x)
        print(y.address)
        h=y.address


        user = authenticate(username=username, password=password,)

        if user:
            if user.is_active :
                if  y.category=='company':
                    login(request,user)
                else:
                    return HttpResponse("not valid.")

                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'user_accounts/complogin.html', {})

