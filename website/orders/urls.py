from django.urls import path
from django.conf.urls import url
from .import views

name_apps = 'Yes_bouquets'

urlpatterns = [

    path('basket_adding/', views.basket_adding, name='basket_adding'),
    path('checkout/', views.checkout, name='checkout'),

]