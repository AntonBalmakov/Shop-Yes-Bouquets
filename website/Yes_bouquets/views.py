from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def landing_view(request):
    return render(request, 'landing/landing.html')