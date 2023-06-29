from django.shortcuts import render

from utils.products.factory import make_product


def home(request):
    return render(request, 'shoppbarth/pages/home.html', context= {'products': [make_product() for _ in range(10)], })


def product(request, id):
    return render(request, 'shoppbarth/pages/product-view.html', context= {'product': make_product, })
