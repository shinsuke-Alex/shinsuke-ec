from django.shortcuts import render
from django.template.response import TemplateResponse
from ec.models import Product

def product_list(request):
    products = Product.objects.order_by('name')
    return TemplateResponse(request, 'ec/product_list.html',
                           {'products': products})
