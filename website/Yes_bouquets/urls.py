from django.urls import path
from django.conf.urls import url
from .views import *

name_apps = 'Yes_bouquets'

urlpatterns = [

    path('landing/', landing_view, name='landing')

]