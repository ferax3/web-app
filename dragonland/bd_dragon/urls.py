from django.urls import path
from . import views

urlpatterns = [
    path('', views.dragons, name='dragons'),
    path('tickets', views.tickets, name='tickets'),
    path('<int:pk>', views.DragonDetailView.as_view(), name='dragon-detail'),
    path('answer', views.answer, name='answer')
]