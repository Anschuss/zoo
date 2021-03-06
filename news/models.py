from django.db import models

class News(models.Model):
    title = models.CharField(max_length=32)
    subject = models.CharField(max_length=120)
    intro = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateTimeField
