from django.db import models
from django.utils import timezone



class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    image = models.ImageField(upload_to='photos/')
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'''{self.first_name},
                    {self.last_name},
                    {self.image},
                    {self.phone},
                    {self.email},
                    {self.password}'''



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
