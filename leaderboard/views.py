from django.shortcuts import render
from user_profile.models import UserProfile

# Create your views here.
def home(request):
    # get top 50
    users = UserProfile.objects.all().order_by('-score')[:50]
    context = {'name': 'LeaderBoard', 'project': 'Django', 'users': users}
    return render(request, 'leaderboard.html', context)
