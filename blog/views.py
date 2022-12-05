from django.shortcuts import render, get_object_or_404
from blog.models import *


def blog_list(request):
    
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)

    context = {
        'post': post
    }

    return render(request, 'blog/blog_detail.html', context)


