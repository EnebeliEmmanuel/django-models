from msilib.schema import Class
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=CASCADE)
    Created_date = models.DateTimeField(auto_now=True)
    Published_date = models.DateTimeField(auto_now=True)
