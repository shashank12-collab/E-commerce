from django.contrib import admin
from .models import Product
from .models import Contact 
from .models import Orders
from .models import OrderUpdate

# Register your models here.
class show(admin.ModelAdmin):
    list_display = ('product_name' , 'pub_date')

admin.site.register(Product , show)
admin.site.register(Contact)

class seen(admin.ModelAdmin):
    list_display = ('order_id' , 'name' , 'State')
    
    
admin.site.register(Orders , seen)
admin.site.register(OrderUpdate)
