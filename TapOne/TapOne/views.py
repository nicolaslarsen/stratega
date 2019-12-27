from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def index(request):
    return render(request, 'index.html')

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
