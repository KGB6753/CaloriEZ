from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from  django.contrib import messages

# Create your views here.
def main(request):
    return render(request, 'diary/main.html')