"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import delete_product, home,about,contact,products,product_detail,create_product,edit_product

#manage.py ----> Django project ko commands dene ka entry point
#settings.py ---> Project Configuration
# /Products ---> urls.py ---> Which view? Django decide karega ki products request ko kis code ke pass bhejna hai
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('about/',about),
    path('contact/',contact),
    path('products/',products,name='products'),
    path('products/<int:id>/',product_detail,name='product_detail'),
    path('products/create/',create_product,name='create_product'),
    path('products/edit/<int:id>/',edit_product,name='edit_product'),
    path('products/delete/<int:id>/',delete_product,name='delete_product')

]
