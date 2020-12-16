from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView,PostDetailView,PostCreateView,PostDeleteView,PostUpdateView,UserPostListView

# app_name = 'blogapp'

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<str:email>/', UserPostListView.as_view(), name='user-post'),


]
