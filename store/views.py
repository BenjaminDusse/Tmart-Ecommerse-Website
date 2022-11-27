from django.shortcuts import render
from django.views.generic import DetailView
from store.models import Product


def home(request):
    return render(request, 'store/index.html')


def products(request):
    return render(request, 'store/shop.html')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    
