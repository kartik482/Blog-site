from django.db import models
from django.contrib import messages

# Create your models here.

class Contact(models.Model):
    
    s_no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    content=models.TextField(max_length=2000)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return "contact from "+self.name +"-"+self.email