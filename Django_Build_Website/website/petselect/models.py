from django.db import models

# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=50)
    hair = models.CharField(max_length=10)
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.name
