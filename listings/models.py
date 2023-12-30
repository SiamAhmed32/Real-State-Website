from django.db import models

# Create your models here.

class Listings(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_b = models.IntegerField()
    sq_footage = models.IntegerField()
    addess = models.CharField(max_length= 100)
    image = models.ImageField()

    def __str__(self):
        return self.title