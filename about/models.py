from django.db import models


class MessageInformation(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=64)
    text = models.TextField()

    def __str__(self):
        return f'{self.email}, {self.subject}'
