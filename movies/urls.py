from django.urls import path
from .views import movie_form

urlpatterns = [
    path('', movie_form, name='movie_form'),
]