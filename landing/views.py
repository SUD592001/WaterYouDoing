from django.shortcuts import render
from django.conf import settings


def landing(request):
    context = {
        'avg_low': settings.AVG_DAILY_WATER_LOW,
        'avg_high': settings.AVG_DAILY_WATER_HI,
    }
    return render(request, 'home.html', context=context)
