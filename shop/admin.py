from django.contrib import admin
from .models import Product

# Register your models here.
class show(admin.ModelAdmin):
    list_display = ('product_name' , 'pub_date')

admin.site.register(Product , show)
