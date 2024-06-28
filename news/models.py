from django.db import models

class New(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()
    category = models.CharField(max_length=50)
    thumnail = models.CharField(max_length=100)
    create_date = models.DateTimeField()