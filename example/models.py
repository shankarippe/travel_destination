from django.db import models

class Destination(models.Model):  # Inheriting from models.Model    
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='images/')  # Ensure media settings are configured
