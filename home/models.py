from django.db import models 
from django.conf import settings
from datetime import datetime

# Create your models here.
class ToDo(models.Model): 
    date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

