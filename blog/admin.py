from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'user',
        'created_on',
        'status',
    )

    list_filter = (
        'status',
    )

class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'comment_content',
        'post',
        'created_on',
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
