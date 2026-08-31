from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_movie, name='random_movie'),
]
