from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/', views.about, name='blog-abaut'),
    path('Register/',views.register, name='user-register'),
    path('Login', views.login, name='user-login'),
    path('Logout/', auth_views.LogoutView.as_view(template_name='blogapp\logout.html'), name='user-logout'),
    path('Profile/', views.profileview, name='user-profile'),

]
