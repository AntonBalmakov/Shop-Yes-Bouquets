from django.urls import path
from django.conf.urls import url
from .views import *

name_apps = 'Yes_bouquets'

urlpatterns = [

    path(r'product/<product_id>', product, name='product')

]