from django import forms
from .models import Product
#Form ---> Modelform ---> Model ---> User
# Model mai jo bhi fields hai uske according form ke liye rules define karne ke liye use hota hai. Jaise ki name, price, quantity ye fields required hai ya nahi, ye form ke liye rules define karne ke liye use hota hai. baar baar na type karna pade isliye ModelForm use kiya hai
class ProductForm(forms.ModelForm):
    # ye form ke liye rules define karne ke liye use hota hai. Jaise ki name, price, quantity ye fields required hai ya nahi, ye form ke liye rules define karne ke liye use hota hai.
    class Meta:
        model = Product
        fields = ['name','price','quantity']
        
    # name = forms.CharField(max_length=100)
    # price = forms.IntegerField()
    # quantity = forms.IntegerField()

