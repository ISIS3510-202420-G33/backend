from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('create', views.user_view, name='museum_create'),
    path('authenticate', views.authenticate_view),
    path('like', views.like_view),
    path('', views.users_view)
    
]