from django.db import models
from django.utils import timezone
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    image = models.ImageField(upload_to='photos/')
    phone = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email','password']
    # objects = BaseUserManager()

    def __str__(self):
        return f'''{self.first_name},
                    {self.last_name},
                    {self.image},
                    {self.phone},
                    {self.email},
                    {self.password}'''

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            newsize = (300,300)
            img.thumbnail(newsize)
            img.rotate(90, Image.NEAREST, expand=1)
            img.save(self.image.path)


class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    userpf = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.email


class Post(models.Model):
    title = models.CharField(max_length=264)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userpost')

    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return f'''{self.title},
                     {self.content},
                     {self.publish},
                     {self.created},
                     {self.author}'''


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})