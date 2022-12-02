from django import template

from store.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return Collection.objects.all()

