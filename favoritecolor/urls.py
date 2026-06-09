from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorite_color, name='favorite_color'),
]