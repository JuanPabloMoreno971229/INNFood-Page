from django.shortcuts import render
from .models import Blog


def blog(request):
    blogs = Blog.objects.all() 
    return render(request, "blog/blog.html", {'blogs': blogs})


def blog_detail(request, id):
    print(id)
    blogs = Blog.objects.filter(id=id)
    print(blogs)
    return render(request, "blog/blog_detail.html", {'blogs': blogs})
