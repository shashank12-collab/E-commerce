from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=1000)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50 , default="")
    price = models.IntegerField(default='0')
    image = models.ImageField(upload_to="shop/images" , default="")
    
    
    def __str__(self):
        return self.product_name
    

class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20 , default="")
    email = models.EmailField(default="")
    number = models.CharField(max_length=15, blank=True)
    desc = models.CharField(max_length=3000 ,default="")
    
    def __str__(self):
        return self.name
    