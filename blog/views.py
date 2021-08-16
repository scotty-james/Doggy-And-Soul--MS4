from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages

from .models import Post


def blog_posts(request):
    """ A view to show all blog posts """

    posts = Post.objects.filter(status=1).order_by('-created_on')
    drafts = Post.objects.filter(status=0).order_by('-created_on')

    context = {
        'posts': posts,
        'drafts': drafts,
    }

    return render(request, 'blog/blog.html', context)