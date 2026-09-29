from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name
'''
models.py ---> makemigrations ---> migration file ---> migrate ---> Database

models file mai kuch bhi change kiya hai toh python manage.py makemigrations command run hogi taaki migration file create hojaaye phir python manage.py migrate command se us file ki help se database mai store karwa sake
'''
