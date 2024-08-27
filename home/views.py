from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


# Create your views here.

from django.shortcuts import render

@login_required
def index(request):
    return render(request, 'home/index.html')
