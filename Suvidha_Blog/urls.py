
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    # path('Logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='user-logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
