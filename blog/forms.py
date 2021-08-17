from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'blog_content', )
        exclude = ('user', 'created_on', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_content',)
