from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from cart.forms import CartAddProductForm
from cart.cart import Cart
from store.models import Product, CartItem


# @register.inclusion_tag('store/tags/shopping_cart_inner.html')
# def get_cart_items():
#     cart_items = CartItem.objects.all()
#     return {"cart_items": cart_items}

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print(cd)
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
        # CartItem.objects.update_or_create(cart=cart, product=product, quantity=cd['quantity'])

    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial= {
                'quantity': item['quantity'],
                'override': True
            }
        )
    context = {
        'cart': cart,
    }
    return render(request, 'cart/detail.html', context)
