from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import get_object_or_404
# Create your views here.

#django is an folder where http handles all about http related things it is a folder. HttpResponse is a file


def home(request):
    return HttpResponse("Welcome to Tushar Website")

def about(request):
    return HttpResponse("I am learning Django Backend")

def contact(request):
    return HttpResponse("Contact Page")

def products(request):
    products = Product.objects.all()
   
    #output = "<h1>Products</h1>"
    #for product in products:
        # output += f"""
        # <h2>{product.name}</h2>
        # <p> Price : {product.price} </p>
        # <p> Quantity : {product.quantity} </p>
        
        # """
        
        # output += f"{product.name} - {product.price} <br>"
    # return HttpResponse(output)
        
    return render(request,'products.html',{'products' : products})



def product_detail(request,id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product,id=id)
    return render(request,'product_detail.html',{'product': product})
#ORM Mental Model
# Python Object ----> Django ORM -----> DataBase Row



