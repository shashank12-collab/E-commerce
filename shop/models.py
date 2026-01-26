from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    pub_date = models.DateField()
    
    
    def __str__(self):
        return self.product_name