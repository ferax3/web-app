from django.shortcuts import render
from .models import Dragon
from django.views.generic import DetailView
# Create your views here.

def dragons(request):
    dragon = Dragon.objects.all()
    return render(request, 'bd_dragon/dragons.html', {'dragon': dragon})

class DragonDetailView(DetailView):
    model = Dragon
    template_name = 'bd_dragon/dragon.html'
    context_object_name = 'information'

def tickets(request):
    return render(request, 'bd_dragon/tickets.html')