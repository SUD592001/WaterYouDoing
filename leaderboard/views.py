from django.shortcuts import render
from landing.models import UserProfile


def leaderboard(request):
    # get top 50
    users = UserProfile.objects.all().order_by('score')[:50]
    context = {'users': users}
    return render(request, 'leaderboard.html', context)
