from django.db import models

# Create your models here.
class Tasklist(models.Model):
    task = models.CharField(max_length=200)
    done = models.BooleanField(default=False)