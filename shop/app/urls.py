from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('shop/', shop, name='shop'),
    path('search/', search, name='search'),
    path('shop/product/<int:product_id>', product, name='product'),

]