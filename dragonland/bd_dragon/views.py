from django.shortcuts import render, redirect
from .models import Dragon, Visitor
from django.views.generic import DetailView
from .forms import VisitForm
# Create your views here.

def dragons(request):
    dragon = Dragon.objects.all()
    return render(request, 'bd_dragon/dragons.html', {'dragon': dragon})

class DragonDetailView(DetailView):
    model = Dragon
    template_name = 'bd_dragon/dragon.html'
    context_object_name = 'information'

def answer(request):
    return render(request, 'bd_dragon/answer.html')
def tickets(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            # Зберігаємо об'єкт моделі Visit
            visit = form.save(commit=False)

            # Витягуємо дані про відвідувача з форми
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            # Створюємо новий об'єкт моделі Visitor і зберігаємо його
            visitor = Visitor.objects.create(first_name=first_name, last_name=last_name, email=email)

            # Прив'язуємо відвідувача до візиту і зберігаємо об'єкт візиту
            visit.visitor = visitor
            visit.save()

            return redirect('answer')  # Перенаправляємо користувача на іншу сторінку після успішного збереження
    else:
        form = VisitForm()

    data = {
        'form': form
    }
    return render(request, 'bd_dragon/tickets.html', data)