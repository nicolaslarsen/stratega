from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm

def index(request):
    return render(request, 'index.html')

def signup(request):
    form = SignUpForm()
    if (request.POST):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Your account was created successfully")
            return redirect('/')
        else:
            messages.error(request, "Account creation was unsuccessful")
    return render(request, 'registration/signup.html', {'form': form})
