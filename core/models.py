from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length= 30)
    body = models.TextField(max_length= None)

    def __str__(self):
        return f'Note title: {self.title} body: {self.body}'


