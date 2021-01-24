from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse
from landing.forms import SignupForm


def landing(request):
    context = {
        'avg_low': settings.AVG_WEEKLY_WATER_LOW,
        'avg_high': settings.AVG_WEEKLY_WATER_HI,
    }
    return render(request, 'home.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        data = form.data
        if form.is_valid():
            # create a user if data is valid
            data = form.cleaned_data
            new_user = User.objects.create_user(data['username'], data['email'], data['password1'])
            new_user.save()
            # log user in
            user = authenticate(username=data['username'], password=data['password1'])
            login(request, user)
            return HttpResponseRedirect(reverse('landing'))
    else:
        form = SignupForm()
    
    context = {'form': form}
    return render(request, 'registration/signup.html', context=context)
