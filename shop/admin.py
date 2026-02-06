from django.contrib import admin
from .models import Product
from .models import Contact

# Register your models here.
class show(admin.ModelAdmin):
    list_display = ('product_name' , 'pub_date')

admin.site.register(Product , show)
admin.site.register(Contact)
