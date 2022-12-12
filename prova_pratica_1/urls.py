from django.urls import path
from prova_pratica_1.views import view_a,view_b,view_c

app_name="prova_pratica_1"
urlpatterns=[
    path('view_a',view_a, name="view_a"),
    path('view_b',view_b, name="view_b"),
    path('view_c',view_c, name="view_c"),
  
]