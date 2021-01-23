from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from user_profile.models import UserProfile


@login_required
def view_profile(request, username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=user)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
