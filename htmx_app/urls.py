from django.urls import path 
from . import views



urlpatterns = [
    path('', views.tabela.as_view(), name='tabela' ),
    path('cadastro', views.cadastro, name='cadastro')
]
