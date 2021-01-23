from django.shortcuts import render, 

# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage (/)")
    context = {'name': 'LeaderBoard', 'project': 'Django'}
    return render(request, 'leaderBoard.html', context)