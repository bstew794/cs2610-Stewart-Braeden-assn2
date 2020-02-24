from django.shortcuts import get_object_or_404, render
from .models import Blog, Comment


def index(request):
    latest_blog_list = Blog.objects.order_by('-posted')[:3]
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'blog/index.html', context)


def archive(request):
    latest_blog_list = Blog.objects.order_by('-posted')
    return render(request, 'blog/archive.html', {'latest_blog_list': latest_blog_list})


def entry(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/entry.html', {'blog': blog})


def about_me(request):
    return render(request, 'blog/about.html')


def tech_tips(request):
    return render(request, 'blog/tips.html')
