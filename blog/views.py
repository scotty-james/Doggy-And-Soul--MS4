from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm


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
    """ A view to show an individual blog post """
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(post=post_id).order_by('-created_on')

    new_comment = None

    """ Adds comment to blog post """

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, 'Comment successfully posted')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Oops, something went wrong! Please try again')
            return redirect(reverse('post_detail', args=[post.id]))
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
        'new_comment': new_comment,
    }

    return render(request, 'blog/post_detail.html', context)


@login_required
def add_post(request):
    """ A view to add blog posts """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
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

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, f'{post.title} Successfully Updated')
            return redirect(reverse('post_detail', args=[post.id]))
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


@login_required
def delete_post(request, post_id):
    """ A view to delete blog posts """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, f'{post.title} Successfully Deleted')
    return redirect(reverse('blog_posts'))


@login_required
def delete_comment(request, comment_id):
    """ A view to delete blog comments """
    
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse('blog_posts'))