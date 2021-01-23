from django.shortcuts import render
from user_profile.models import UserProfile


def view_profile(request, username):
    user = UserProfile.objects.get(username=username)
    context = {'name': 'Profile', 'project': 'Django', 'user': user}
    return render(request, 'profile.html', context)
