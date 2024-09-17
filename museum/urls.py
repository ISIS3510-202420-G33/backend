from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.museums_view, name='museum_view')
]