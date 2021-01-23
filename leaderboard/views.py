from django.shortcuts import render, 

# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage (/)")
    users = UserProfile.objects.all().order_by('score')
    context = {'name': 'LeaderBoard', 'project': 'Django', 'users': users}
    return render(request, 'leaderBoard.html', context)
