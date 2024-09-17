from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.artwork_view, name='artwork_view')
]