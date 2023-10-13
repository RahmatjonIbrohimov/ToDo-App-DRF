from django.db import models


# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=30)
    descriptions = models.TextField(blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'Title: {self.title}'
    