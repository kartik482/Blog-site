from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Post(models.Model):
    s_no=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    content=models.TextField()
    views=models.IntegerField(default=0)
    author=models.CharField(max_length=13)
    slug=models.CharField(max_length=130)
    timestamp=models.DateTimeField(blank=True)
    

    def __str__(self):
        return self.title


class Blogcomment(models.Model):
    s_no=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey("self",on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:15]+"..."+" by "+self.user.email
    
