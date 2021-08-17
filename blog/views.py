from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm


def blog_posts(request):
    """ A view to show all blog posts """

    posts = Post.objects.filter(status=1).order_by('-created_on')
    drafts = Post.objects.filter(status=0).order_by('-created_on')

    context = {
        'posts': posts,
        'drafts': drafts,
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)


@login_required
def add_post(request):
    """ A view to add blog posts """
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            form_data = post_form.save(commit=False)
            form_data.user = request.user
            form_data.save()
            messages.success(request, 'Your blog was posted successfully!')
            return redirect('blog_posts')
        else:
            messages.error(request, 'Oops, something went wrong! Please try again')
            return redirect('add_post')
    else:
        post_form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'post_form': post_form,
    }
    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """ A view to edit blog posts """
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            messages.success(
                request, f'{post.title} Successfully Updated')
            return redirect('blog_posts')
        else:
            messages.error(request, f'Something went wrong, {post.title} not updated please try again')
    else:
        post_form = PostForm(instance=post)
        messages.info(request, f'You are currently editing {post.title}')

        template = 'blog/edit_post.html'
        context = {
            'post_form': post_form,
            'post': post,
        }

        return render(request, template, context)