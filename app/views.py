from django.shortcuts import render
from .models import Task

def home_view(request):
    # Получаем все задачи из базы данных
    tasks = Task.objects.all()
    # Передаем задачи в HTML-шаблон
    return render(request, 'index.html', {'tasks': tasks})