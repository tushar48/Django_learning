
from django.urls import path
from .views import home,about,contact,products,product_detail,create_product,edit_product,delete_product
urlpatterns =[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('products/',products,name='products'),
    path('products/<int:id>/',product_detail,name='product_detail'),
    path('products/create/',create_product,name='create_product'),
    path('products/edit/<int:id>/',edit_product,name='edit_product'),
    path('products/delete/<int:id>/',delete_product,name='delete_product')
    
]