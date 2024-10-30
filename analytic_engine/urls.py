from django.urls import path
from . import views

urlpatterns = [
    path('recommend/<int:user_id>', views.recommend_view),    
    path('nearest-museums/', views.nearest_museums_view), 
    path('mostliked/', views.most_liked_artwork_view),
    path('spotlights/', views.spotlight_artworks_view), 
]