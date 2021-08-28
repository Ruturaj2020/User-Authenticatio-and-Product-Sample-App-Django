from django.http import request
from django.shortcuts import render,HttpResponse
from products.models import productview
# Create your views here.

def product(request):
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        weight = request.POST.get('weight')
        price = request.POST.get('price')
        prods = productview(product_name=product_name, weight=weight, price=price)
        prods.save()
    return render(request, 'product/pro.html')