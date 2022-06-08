from django.urls import path
from utility import views

urlpatterns = [
    path('', views.index, name='index'),   
]