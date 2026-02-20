import json
from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Product , Contact , Orders , OrderUpdate
from shop.models import Orders
from math import ceil

# Create your views here.

def index(request):
   allprod = []
   catprods = Product.objects.values('category' , 'id')
   cats = {item['category'] for item in catprods}
   for cat in cats:
       prod = Product.objects.filter(category = cat)
       n = len(prod)
       nslides = n//4 + ceil((n/4) - (n//4))
       allprod.append([prod , range(1 , nslides) , nslides]) 
   prod = {'allprod':allprod}
   return render(request ,'shop/index.html' , prod)   

def about(request):
    
    return render(request ,'shop/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name' , "")
        email = request.POST.get('email' , "")
        number = request.POST.get('number' , "")
        desc = request.POST.get('desc' , "")
        contact = Contact(name = name , email=email , number = number , desc = desc)
        contact.save()
    return render(request ,"shop/contact.html")

def tracker(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')

        orders = Orders.objects.filter(order_id=orderId, Email=email)

        if orders.exists():
            updates_qs = OrderUpdate.objects.filter(order_id=orderId)

            updates = []
            for item in updates_qs:
                updates.append({
                    'text': item.update_desc,
                    'time': str(item.timestamp)
                })
        
            response = json.dumps(updates)
            return HttpResponse(response, content_type='application/json')

        else:
            return HttpResponse(json.dumps([]), content_type='application/json')

    return render(request, 'shop/tracker.html')
    

def search(request):
    return render(request , 'shop/search.html')

def productview(request , id):
    #fetch the product using the id
    product = Product.objects.filter(id = id)
    print(product)
    return render(request ,'shop/product.html' , {'product' : product[0]})

def checkout(request):
    thank = False
    id = None
    if request.method == "POST":
        print(request.POST) 

        items = request.POST.get('items_json', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone_number = request.POST.get('phone_number', "")
        address = request.POST.get('address1', "") + " " + request.POST.get('address2', "")
        state = request.POST.get('state', "")
        city = request.POST.get('city', "")
        zip_code = request.POST.get('zip_code', "")

        order = Orders(
            items_json=items,
            name=name,
            Email=email,
            phone_number=phone_number,
            address=address,
            State=state,
            city=city,
            zip_code=zip_code
        )
        order.save()
        update = OrderUpdate(order_id = order.order_id , update_desc = "The order has been placed")
        update.save()
        thank = True
        id = order.order_id
    return render(request, 'shop/checkout.html' , {'thank':thank , 'id':id})

def home(request):
    return render(request , 'shop/index.html')



