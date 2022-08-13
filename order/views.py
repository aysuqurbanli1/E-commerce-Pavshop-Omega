from email.mime import base
from itertools import product
from math import prod
import sys, json
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
# from order.models import BillingDetail
from order.forms import ShippingDetailForm
from django.http import JsonResponse
from order.models import Basket, BasketItem, Order
from product.models import ProductVersion
import requests
from django.contrib.auth import get_user_model, authenticate


def checkout(request):
    total=20.00
    form=ShippingDetailForm()
    if request.method=='POST':  
        form=ShippingDetailForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('form is valid')

    context={
        'form':form,
        'total':total

    }
    return render(request, 'checkout.html',context)



def shoppingcart(request):
    return render(request, 'shopping-cart.html')

 
