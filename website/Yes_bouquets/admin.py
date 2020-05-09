from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):  # форма админки
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['name']      #отображение по имени
    search_fields = ['name', 'email']   #фильтрация по имени и емайлу
    fields = ['email']

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
