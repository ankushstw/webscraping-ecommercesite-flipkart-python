from django.urls import path
from dworld import views

urlpatterns = [
    path('', views.dworld, name='dworld'),
]