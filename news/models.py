import datetime
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Them(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=32)
    them = models.ForeignKey(Them, on_delete=models.CASCADE, blank=True)
    subject = models.CharField(max_length=120)
    intro = models.CharField(max_length=300)
    text = models.TextField()
    tags = models.ManyToManyField(Tag)
    date = models.DateTimeField()

    def __str__(self):
        return self.title, self.subject, self.them

