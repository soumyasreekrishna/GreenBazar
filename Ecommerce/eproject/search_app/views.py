from django.shortcuts import render
from django.template import RequestContext
from eapp.models import Product
from django.db.models import Q




def do_search(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) )
        return render(request,'search.html',{'query':query,'products':products})



