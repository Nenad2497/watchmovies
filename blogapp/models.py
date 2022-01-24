from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime ,date

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images")

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    header_image = models.ImageField(null = True, blank=True,upload_to="")
    date_added = models.DateField(auto_now_add=True)
    trailer_link = models.CharField(max_length=255,default="no link")
    category = models.CharField(max_length=255,default="undefined")
    
    def __str__(self):
        return self.title +  ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

