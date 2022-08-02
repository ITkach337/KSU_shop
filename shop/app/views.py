from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Product
from .forms import UpdateProduct
from .forms import *
from django.core.paginator import Paginator
from django.db.models import Q
import math
from cart.forms import CartAddProductForm
from django.conf import settings


def index(request):
    return render(request, 'shop/index.html')


# search product
def search(request):
    search_query = request.GET.get('search_query', None) or request.POST.get('search_query', '')
    product = Product.objects.filter(name__icontains=search_query)
    context = {
        'prod': product,
        'search_query': search_query,
    }
    return render(request, 'shop/search.html', context)


# print all products
def shop(request):
    product = Product.objects.all()
    context = {
        'prod': product,

    }
    return render(request, 'shop/shop.html', context)




# print one product
def product(request, product_id,):
    product = get_object_or_404(Product,
                                id=product_id),
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product.html',
                  {'product': product, 'cart_product_form': cart_product_form})






