from django.db import models

# Create your models here.
class Enchere(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    typelot = models.CharField(max_length=255, choices=[('Electronics & Gadgets','Electronics & Gadgets'),
                                                         ('Fashion & Accessories','Fashion & Accessories'),
                                                         ('Home & Furniture','Home & Furniture'),
                                                         ('Vehicles & Automotive','Vehicles & Automotive'),
                                                         ('Collectibles & Art','Collectibles & Art')])
    
    typevente = models.CharField(max_length=255, choices=[('Auction','Auction'),
                                                         ('Sale','Sale')])
    seller = models.ForeignKey('users.User', on_delete=models.CASCADE)
    soldprice = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    
    
    def __str__(self):
        return self.name
