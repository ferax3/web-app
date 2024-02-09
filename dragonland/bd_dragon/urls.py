from django.urls import path
from . import views

urlpatterns = [
    path('', views.dragons, name='dragons'),
    path('<int:pk>', views.DragonDetailView.as_view(), name='dragon-detail')
]