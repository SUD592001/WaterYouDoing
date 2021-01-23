from django.shortcuts import render
from evaluator.forms import EvaluatorForm
from user_profile.models import UserProfile

# Create your views here.
def evaluate(request):
    if request.method == 'POST':
        # get form data from post
        form = EvaluatorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # calculate score = laundry loads
            score = int(data['weekly_laundry_loads'])
            
            # if profile with given username already exists, update profile. 
            # otherwise make profile for user
            try:
                profile = UserProfile.objects.get(username=data['username'])
                profile.score = score
            except UserProfile.DoesNotExist:
                profile = UserProfile(username=data['username'], score=score)
            
            # store profile in db
            profile.save()
    else:
        form = EvaluatorForm()

    context = {
        'form': form
    }
    return render(request, 'evaluate.html', context=context)
