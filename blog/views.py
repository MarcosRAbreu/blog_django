from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    # posts = Post.objects.get(pk=1)
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html', context)

def post_detail(request, post_id):
    posts = Post.objects.get(pk=post_id)

    context = {
        'posts' : posts
    }
    return render(request,'blog/post_detail.html', context)


