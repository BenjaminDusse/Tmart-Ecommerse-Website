from django.contrib import admin
from blog.models import *

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     fields = ['author', 'product', 'tags', 'title', 'slug', 'description', 'slogan', 'image']
#     list_display = ['title', 'slogan', 'image', 'author']

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
