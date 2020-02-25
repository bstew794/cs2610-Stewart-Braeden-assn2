import datetime

from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, Comment
from .forms import CommentForm


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


def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.posted = datetime.datetime.now()
            comment.save()
            return redirect('./', pk=blog_id)

    else:
        form = CommentForm()

    return render(request, 'blog/add_comment.html', {'form': form})


def about_me(request):
    return render(request, 'blog/about.html')


def tech_tips(request):
    return render(request, 'blog/tips.html')
