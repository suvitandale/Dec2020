from django.contrib import admin
from .models import Post,User,Login
class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        fields = '__all__'

admin.site.register(Post,PostAdmin)


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User
        fields = '__all__'

admin.site.register(User,UserAdmin)


class LoginAdmin(admin.ModelAdmin):
    class Meta:
        model = Login
        fields = '__all__'

admin.site.register(Login,LoginAdmin)

