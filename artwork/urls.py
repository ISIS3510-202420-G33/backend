from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.artwork_view),
    path('comments/<int:pk>', views.artwork_comments_view),
    path('artist/<int:pk>', views.artworks_by_artist_view),
    path('museum/<int:pk>', views.artworks_by_museum_view),
    path('', views.artworks_list_view)
]