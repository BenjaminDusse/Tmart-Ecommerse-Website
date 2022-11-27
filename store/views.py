from django.shortcuts import render

def home(request):
    return render(request, 'store/index.html')


def products(request):
    return render(request, 'store/shop.html')
