from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_hero, name='all_hero'),
    path('<int:hero_id>/',views.hero_detail, name='hero_detail'),
    path('hero_stores/',views.hero_store_view, name='hero_stores'),
]
