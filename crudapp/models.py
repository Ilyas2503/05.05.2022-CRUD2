from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length=50)
    message = models.TextField()
    publish_date = models.DateField()
# Create your models here.
