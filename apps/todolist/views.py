from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.urls import reverse


def hello_view(request):
    return HttpResponse('Python goes brrr......')
def reverse_view(request):
    return HttpResponse(reverse('hello'))