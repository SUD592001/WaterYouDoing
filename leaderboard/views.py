from django.shortcuts import render, HttpResponse
from user_profile.models import UserProfile


# Create your views here.
def test(request):
    users = UserProfile.objects.all().order_by('score')
    print(users)
    return HttpResponse(request, users[0])
