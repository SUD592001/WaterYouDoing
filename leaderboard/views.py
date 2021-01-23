from django.shortcuts import render
from user_profile.models import UserProfile

# Create your views here.
def home(request):
    users = UserProfile.objects.all().order_by('-score')
    context = {'name': 'LeaderBoard', 'project': 'Django', 'users': users}
    return render(request, 'leaderBoard.html', context)
