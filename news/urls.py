from django.urls import path
from .views import home, ArticoloDetailViewCB, ArticoloListView, GiornalistaDetailViewCB, GiornalistaListView, giornalisti_list_api, articoli_list_api, giornalista_api, articolo_api, tabella_giornalisti, tabella_articoli, #articoloDetailView

app_name= 'news'

urlpatterns=[
    path('',home, name="homeview"),
    #path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
    path("articoli/<int:pk>", ArticoloDetailViewCB.as_view(), name="articolo_detail"),
    path("lista_articoli/", ArticoloListView.as_view(), name="lista_articoli"),
    #path("lista_giornalisti/", ArticoloListView.as_view(), name="lista_giornalisti")
    path("giornalisti/<int:pk>", GiornalistaDetailViewCB.as_view(), name="giornalista_detail"),
    path("lista_giornalisti/", GiornalistaListView.as_view(), name="lista_giornalisti"),

    path("giornalisti_list_api/", giornalisti_list_api,name="giornalisti_list_api"),
    path("articoli_list_api/", articoli_list_api,name="articoli_list_api"),
    path("giornalista_api/<int:pk>", giornalista_api,name="giornalista_api"),
    path("articolo_api/<int:pk>", articolo_api,name="articolo_api"),
    path("tabella_giornalisti/", tabella_giornalisti,name="tabella_giornalisti"),
    path("tabella_articoli/", tabella_articoli,name="tabella_articoli"),

]
