
from multiprocessing import context
import random
from django.shortcuts import render

def somma(request):
    n1=random.randint(1,10)
    n2=random.randint(1,10)
    context={
        'n1':n1,
        'n2':n2,
        's': n1 + n2
    }
    return render(request,"maxmin.html",context)

def media(request):
    lista=[]
    for i in range(30):
        lista.append(random.randint(1,10))
    context={
        'lista':lista,
        'media': sum(lista)/len(lista)
    }
    return render(request,"media.html",context)

def index3(request):
    return render(request,"index3.html")

