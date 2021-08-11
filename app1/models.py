from django.db import models

# Create your models here.
class Todo(models.Model):
    name=models.CharField(max_length=100,default='NULL')
    content=models.TextField()
    complete=models.BooleanField(default=False)