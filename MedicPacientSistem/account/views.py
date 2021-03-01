from django.shortcuts import render
from django.contrib.auth import login, logout
from .forms import *
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from user_profile.models import UserProfile


# Create your views here.

def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'abouts.html')


def contact(request):
    return render(request, 'contact.html')


def SignUp(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = user.first_name
            last_name = user.last_name
            name = first_name + ' ' + last_name
            UserProfile.objects.create(name=name, user=user)
            login(request, user)
            return redirect('account:home')
    else:
        form = UserCreateForm()
    return render(request, 'signup.html', {'form': form})
