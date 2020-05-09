from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscribeForm
# Create your views here.


def landing_view(request):
    name = "landing_view"
    form = SubscribeForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.changed_data
        new_form = form.save()

    return render(request, 'landing/landing.html', locals())