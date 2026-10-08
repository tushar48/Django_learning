from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.shortcuts import get_object_or_404
from django.contrib import messages

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


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST) # django ye user ka submitted data hai. Is data ko mere ProductForm ke rules ke according process karo
        
        if form.is_valid():
            form.save() # ye form ke data ko save kar dega database me. Ye automatically cleaned_data ka use karke data ko python ke according convert kar deta hai aur fir database me save kar deta hai.
            
            # name = form.cleaned_data['name']
            # price = form.cleaned_data['price'] #user ne jo data diya hai might be string ho sakta hai toh usko cleaned ya convert karne ke liye django ka cleaned_data use karte hai. Ye data ko python ke according convert kar deta hai.
            # quantity = form.cleaned_data['quantity']
            #Product.objects.create(name=name,price=price,quantity=quantity)
            messages.success(request,"Product Successfully Created")
            return redirect('products')
    else:
        form = ProductForm()

        
    return render(request,'create_product.html',{'form':form})



#Remember this line 
#Django form user ka input leta hai check karta hai clean karta hai ModelForm ke case main valid data ko model ke through database main save karne mai help karta hai
def edit_product(request,id):
    product = Product.objects.get(id=id)
    
    if request.method == "POST":
        form = ProductForm(request.POST,instance=product) # iska matlab hai ki edit ka button dabate hi user ka data form me aa jayega aur fir user usko edit kar sakta hai. instance=product ka matlab hai ki ye form ke liye rules define karne ke liye use hota hai. Jaise ki name, price, quantity ye fields required hai ya nahi, ye form ke liye rules define karne ke liye use hota hai. 

        if form.is_valid():
            form.save()
            messages.success(request,"Product Successfully Updated")
            return redirect('products')
        
    else:
        form = ProductForm(instance=product)


    return render(request,'edit_product.html',{'form':form})

def delete_product(request,id):
    if request.method == "POST":
        product = get_object_or_404(Product,id=id)
        product.delete()
        messages.success(request,"Product Successfully Deleted")
        return redirect("products")
    # product.delete()
    messages.success(request,"Product Successfully Deleted")
    return redirect('products')
