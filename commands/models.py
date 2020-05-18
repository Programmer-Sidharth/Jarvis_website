from django.db import models

# Create your models here.

class Command(models.Model):
    hotword = models.CharField(max_length=100)
    hotword2 = models.CharField(max_length=100)
    output = models.CharField(max_length=1000)
    output2 = models.CharField(max_length=1000)
    output3 = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.hotword} | {self.hotword2}"
    
