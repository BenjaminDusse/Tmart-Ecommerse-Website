from decimal import Decimal
from django.conf import settings
from store.models import *

class Cart(object):
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product: Product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'unit_price': str(product.unit_price)}

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity

        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product: Product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['unit_price'] = Decimal(item['unit_price'])
            item['total_price'] = item['unit_price'] * item['quantity']
            yield item

        
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_subtotal_price(self, product: Product):
        print(sum(Decimal(item['quantity'] * product.unit_price) for item in self.cart.values()))
        return sum(Decimal(item['quantity'] * product.unit_price) for item in self.cart.values())


    def get_total_price(self):
        return sum(Decimal(item['unit_price'] * item['quantity']) for item in self.cart.values())

    def clean(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

# Cart object looks like this
# Cart = {
#     'product': {
#         'quantity',
#         'unit_price'
#     }
# }