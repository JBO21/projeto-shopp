from django.urls import path

from shoppbarth.views import home

urlpatterns = [
    path('', home),   
]