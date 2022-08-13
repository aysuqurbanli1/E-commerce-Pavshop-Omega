from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from blog.models import Blog
from django.db.models import Count
from core.models import Contact
from core.forms import ContactForm, SubscribeForm
from product.models import ProductVersion


def home(request):
    print(request.user.is_authenticated)
    products=ProductVersion.objects.all().order_by('-created_at')[:8]
    popular = ProductVersion.objects.annotate(chapters_cnt=Count('reviews')).order_by('-chapters_cnt')[:8]
    slide=ProductVersion.objects.all().order_by('-created_at')[:2]
    context = {
        'products': products,
        'popular':popular,
        'slide':slide
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about-us.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST' and 'contactform' in request.POST:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Melumatlar qeyde alindi!')
            return redirect(reverse_lazy('contact'))
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)



def search(request):
    print("AAAAAAAAAAAAAAAAAAA")
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        products= ProductVersion.objects.filter(title__icontains = q)
    else:
        products=ProductVersion.objects.all()
    context={
            'products':products,
    }
    return render(request, 'product-list.html',context)



# def search(request):
#     if 'q' in request.GET and request.GET['q']:
#         q = request.GET['q']
#         product_item = ProductVersion.objects.filter(title__icontains = q)
#         context={
#             'product_item':product_item,
#         }
#         return render(request, 'product-list.html',context)

#     else:
#         return HttpResponse('Please submit a search term.')
 
# def search(request):
#      if request.method =="POST":
#          q=request.POST['q']
#          product_item = Product.objects.filter(title__icontains = q)
#          return render(request, 'product-list.html',{'product_item':product_item,'query': q})