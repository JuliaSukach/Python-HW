from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.main, name='home'),
    path('food', views.food, name='food'),
    path('exercise', views.exercise, name='exercise'),
    path('reports', views.reports, name='reports'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
