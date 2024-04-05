from django.urls import path
from expense import views

urlpatterns = [
    path('', views.index, name='index'),
]