from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('<int:pk>', views.artist_view, name='artist_view'),
    path('', views.artist_list_view, name='create_artist') 
]
