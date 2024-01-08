from django.urls import path
from .views import main, create_product

urlpatterns = [
    path('', main, name='main'),
    path('create_product', create_product, name='create_product')
]