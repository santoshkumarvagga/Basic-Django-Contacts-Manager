from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='showit'),
    path('add/', views.add, name = 'addit'),
    path('edit/<int:cid>/', views.edit, name = 'editit'),
    path('modify/<int:cid>/', views.modify, name = 'modifyit'),
    path('alter/<int:cid>/', views.alter, name = 'alterit'),
]