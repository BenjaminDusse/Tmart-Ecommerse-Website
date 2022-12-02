from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from store.models import Product, ProductImage, Collection
from cart.forms import CartAddProductForm

def home(request):
    collections = Collection.objects.only('title', 'parent').filter(parent_id__isnull=True)
    # parent_id = request.
    # collection_children = Collection.objects.filter(parent_id__isnull=False)
    
    context = {
        'collections': collections,
        # 'collection_children': collection_children,
    }

    return render(request, 'store/index.html', context)


def products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'store/product_list.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'store/product_detail.html', context)

# collections = Collection.objects.filter(parent_id__isnull=True)

# collection_children = Collection.objects.filter(parent_id = 1) # need find parent_id first and edit like that parent_id=parent_id


# childrens_children = Collection.objects.filter(parent_id__isnull=False)