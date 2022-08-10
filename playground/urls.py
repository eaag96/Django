from django.urls import path
from . import views

urlpatterns= [
    path('Hello/',views.say_hello)
]