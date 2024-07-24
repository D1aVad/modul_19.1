from django.db import models

# Create your models here.

class Bayer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(decimal_places=2, max_digits=6)
    age = models.IntegerField()


    def __str__(self):
        return self.name
    
class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    size = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    age_limited = models.BooleanField(True)
    buyer = models.ManyToManyField(Bayer, related_name='bayer')