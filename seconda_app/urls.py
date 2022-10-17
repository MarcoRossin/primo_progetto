from django.urls import path
from seconda_app.views import es_if,if_else_elif,ciclo_for,index2

app_name="seconda_app"
urlpatterns=[
    path('es_if',es_if,name="es_if"),
    path('if_else_elif',if_else_elif,name='if_else_elif'),
    path('ciclo_for',ciclo_for,name='ciclo_for'),
    path('index2',index2,name='index2'),
]