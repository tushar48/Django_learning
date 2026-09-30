from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.PositiveBigIntegerField(default=0)
    
    
    def __str__(self):
        return self.name
    
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name

'''
models.py ---> makemigrations ---> migration file ---> migrate ---> Database

models file mai kuch bhi change kiya hai toh python manage.py makemigrations command run hogi taaki migration file create hojaaye phir python manage.py migrate command se us file ki help se database mai store karwa sake
'''

'''
After creating the object
object.save() then this is the mechanism save() --> Django ORM --> Database
#Method - 1
product = Product(name="Laptop",price=50000,quantity=5)
product.save()

#Method - 2

Product.objects.create(name="Mouse",price=20000,quantity=2)
It will create the object and save simultaneously


QuerySet ---> Queryset Django orm ka object hai jo database queries ko represent ya manage karta hai
Django Querysets are lazy
It will evaluate later not calculate each and everything at once

When we use Product.objects.filter(price=50000) 
return queryset
might be 
0 objects
1 objects
10 objects

When we use Product.objects.get(name="Mouse")
it will return one thing not many
if its not found then return doesnotexist

Use get when you have only one object or one objects is reside into your QuerySet

If you want to upadte multiple queryset then you can do just like this
Product.objects.filter(price=50000).update(price=500)


'''
