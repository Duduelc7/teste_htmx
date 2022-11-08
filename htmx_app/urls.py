from django.urls import path 
from . import views



urlpatterns = [
    path('', views.empresa, name='empresa_list'),
    path('create/', views.empresa_create, name='empresa_create'),
    path('create-contact/', views.create_contact, name='create-contact'),
    path("contacts/", views.ContactList.as_view(), name='contact-list'),
    path('create-regiao/', views.create_regiao, name='create-regiao'),
    path('regiao/',views.RegioesList.as_view(), name='regiao-list')
]