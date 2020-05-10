from django.urls import path
from django.conf.urls import url
from .views import *

name_apps = 'Yes_bouquets'

urlpatterns = [

    path(r'^product/(?P<product_id>\w+)/$', product, name='product')

]