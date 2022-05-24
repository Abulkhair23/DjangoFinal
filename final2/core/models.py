import os

from django.db import models

# Create your models here.

class Book(models.Model):
    num_pages = models.CharField(max_length=100, blank=True, default="")
    genre = models.TextField(max_length=1000, blank=True, default="")
    
class Journal(models.Model):
    type = models.TextField(max_length=1000, blank=True, default="")
    publisher = models.TextField(max_length=1000, blank=True, default="")


