from django.shortcuts import render, get_object_or_404
from blog.models import *
from blog.forms import CommentForm

def blog_list(request):
    
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)

    # comments
    comments = post.comments.filter(active=True)

    # commentform
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_form = form.save()
            comment_form.post = post
            comment_form.user = request.user
            comment_form.save()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, 'blog/blog_detail.html', context)
