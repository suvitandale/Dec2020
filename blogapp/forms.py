from .models import User,Login
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['email','password']