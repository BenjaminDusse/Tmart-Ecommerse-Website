from django.shortcuts import render

def login(request):

    if request.met

    return render(request, 'auth/login.html')

def register(request):
    return render(request, 'auth/register.html')