from django.urls import path
from libfarhan import a

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

print(a())
