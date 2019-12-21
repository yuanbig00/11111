from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
class UsersProfile(AbstractUser):
#class User(AbstractUser):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    # name = models.CharField(max_length=128, unique=True)
    name=models.ForeignKey('self',on_delete=models.CASCADE,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=(("male",u"男"),("female",u"女")),default="male")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

