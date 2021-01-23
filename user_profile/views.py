from django.shortcuts import render
from user_profile.models import UserProfile
# Create your views here.
def view_profile(request):
    users = UserProfile.objects.all().order_by('-score')
    context = {'name': 'Profile', 'project': 'Django', 'users': users}
    return render(request, 'profile.html', context)git