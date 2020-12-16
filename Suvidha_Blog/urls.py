
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include,reverse_lazy
from django.conf.urls.static import static
from . import settings
from blogapp import views as user_views
from django.conf.urls import url


urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('about/', user_views.about, name='blog-abaut'),
    path('Register/',user_views.register, name='user-register'),
    path('Login', user_views.login, name='user-login'),
    path('Profile/', user_views.profileview, name='user-profile'),
    path('Logout/', auth_views.LogoutView.as_view(template_name='blogapp\logout.html'), name='user-logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='blogapp/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='blogapp\password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='blogapp\password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='blogapp/password_reset_complete.html'),name='password_reset_complete'),
    path('', include('blogapp.urls')),

  ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#