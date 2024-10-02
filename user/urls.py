from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('create', views.user_view, name='museum_create'),
    path('authenticate', views.authenticate_view),
    path('like', views.like_view),
    path('liked/<int:pk>', views.liked_view),
    path('liked/<int:user_id>/<int:artwork_id>', views.unlike_view, name='unlike_artwork'), 
    path('', views.users_view)
]