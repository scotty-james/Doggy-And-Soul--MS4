from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts, name='blog_posts'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
]