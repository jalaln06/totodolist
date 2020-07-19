from django.contrib import admin
from django.urls import path

from apps.todolist.views import hello_view, reverse_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('reverse/', reverse_view, name='reverse'),
]