from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse

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

class ArticoloDetailViewCB(DetailView):
    model= Articolo
    template_name= "articolo_detail.html"

class ArticoloListView(ListView):
    model= Articolo
    template_name= "lista_articoli.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["articoli"] = Articolo.objects.all()
        return context
    
class GiornalistaDetailViewCB(DetailView):
    model= Giornalista
    template_name= "giornalista_detail.html"

class GiornalistaListView(ListView):
    model= Giornalista
    template_name= "lista_giornalisti.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["giornalisti"] = Giornalista.objects.all()
        return context

def giornalisti_list_api(request):
    giornalisti=Giornalista.ojects.all()
    data={'giornalisti':list(giornalisti.values("pk","nome","cognome"))}
    response=JsonResponse(data)
    return response

def giornalista_api(request,ok):
    try:
        giornalista=Giornalista.ojects.get(pk=pk)
        data={'giornalista':{
            "nome":giornalista.nome,
            "cognome":giornalista.cognome,
            }    
        }
        response=JsonResponse(data)
    except Giornalista.DoesNoExist:
        response=JsonResponse({
            "error":{
                "code":404,
                "message":"Giornalista non trovato"
            }},
            status=404)
    return response

def articoli_list_api(request):
    articoli=Articolo.ojects.all()
    data={'articoli':list(articoli.values("titolo","contenuto","giornalista"))}
    response=JsonResponse(data)
    return response

def articolo_api(request,ok):
    try:
        articolo=Articolo.ojects.get(pk=pk)
        data={'articolo':{
            "titolo":articolo.nome,
            "giornalista":articolo.cognome,
            }    
        }
        response=JsonResponse(data)
    except Articolo.DoesNoExist:
        response=JsonResponse({
            "error":{
                "code":404,
                "message":"Articolo non trovato"
            }},
            status=404)
    return response


def tabella_giornalisti(request):
    return render(request, "tabella_giornalisti.html")

def tabella_articoli(request):
    return render(request, "tabella_articoli.html")



