from django.shortcuts import render
from django.views.generic import DetailView
from store.models import Product, ProductImage


def home(request):
    return render(request, 'store/index.html')


def products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'store/product_list.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'

def product_detail(request, pk):
    product = Product.objects.get(id=pk)

    context = {
        'product': product,
    }
