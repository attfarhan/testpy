from django.urls import path
from libfarhan import testfunc

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

print(testfunc())
