from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('user', )

    list_display = (
        'title',
        'user',
        'created_on',
        'status',
    )

    list_filter = (
        'status',
    )

admin.site.register(Post, PostAdmin)
