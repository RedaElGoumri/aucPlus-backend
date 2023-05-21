from django.db import models

# Create your models here.
class Enchere(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    typelot = models.EmailField(max_length=255)
    typevente = models.CharField(max_length=255)
    responsable = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name
