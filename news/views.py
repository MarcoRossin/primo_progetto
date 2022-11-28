"""from django.http import HttpResponse
from .models import Articolo, Giornalista

# Create your views here.
def home(request):
    #a= ""
    a=[] # lista
    #g= ""
    g=[] # lista
    for art in Articolo.objects.all():
        #a +=(art.titolo + "<br>")
        a.append(art.titolo)
    for gio in Giornalista.objects.all():
        #g +=(gio.nome + "<br>")
        g.append(gio.nome) # utilizzo append perchè è una lista 
    #response= "Articoli:<br>" + a + "<br>Giornalisti:<br>"+ g
    response= str(a) + "<br>" + str(g) #trasformo le liste in stringhe 
    print(response)

    return HttpResponse("<h1>"+ response + "</h1>")"""

from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista

def home(request):
    articoli= Articolo.objects.all()
    giornalisti= Giornalista.objects.all()
    context= {"articoli":articoli,"giornalisti":giornalisti}
    print(context)
    return render(request, "home.html", context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context={"articolo": articolo}
    return render(request, "articolo_detail.html", context)


