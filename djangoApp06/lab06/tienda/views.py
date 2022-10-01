from itertools import product
from multiprocessing import context
from django.shortcuts import render
from .models import Producto
# Create your views here.
def index(request):
    product_list=Producto.objects.all()
    context={
        'product_list':product_list
    }
    return render(request,'index.html',context)