from django.forms import ModelForm
from store.models import *

class CartItemForm(ModelForm):

    class Meta:
        model = CartItem
        fields = '__all__'
        