from django.db import models

# Create your models here.

class TodoItem(models.Model):
    item = models.TextField(max_length=10)