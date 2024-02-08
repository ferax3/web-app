from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('reserve', views.reserve, name='reserve'),
    path('to_do', views.to_do, name='to_do'),
    path('map', views.map, name='map')
]