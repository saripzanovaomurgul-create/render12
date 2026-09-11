from django.urls import path
from .views import home_view

urlpatterns = [
    # Главная страница приложения
    path('', home_view, name='home'),
]