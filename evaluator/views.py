from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from evaluator.forms import EvaluatorForm
from user_profile.models import UserProfile

# Create your views here.
def evaluate(request):
    if request.method == 'POST':
        # get form data from post
        form = EvaluatorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # if profile with given username already exists, update profile. 
            # otherwise make profile for user
            try:
                profile = UserProfile.objects.get(username=data['username'])
                profile.weekly_laundry_loads = data['weekly_laundry_loads']
                profile.daily_bathroom_trips = data['daily_bathroom_trips']
                profile.weekly_showers = data['weekly_showers']
                profile.shower_times = data['shower_times']
                profile.weekly_baths = data['weekly_baths']
                profile.weekly_dishes = data['weekly_dishes']
                profile.weekly_sprinkler = data['weekly_sprinkler']
                profile.swimming_pool = data['swimming_pool']
            except UserProfile.DoesNotExist:
                profile = UserProfile(username=data['username'], weekly_laundry_loads = data['weekly_laundry_loads'],
                                      daily_bathroom_trips = data['daily_bathroom_trips'],
                                      weekly_showers = data['weekly_showers'], shower_times = data['shower_times'],
                                      weekly_baths = data['weekly_baths'], weekly_dishes = data['weekly_dishes'],
                                      weekly_sprinkler = data['weekly_sprinkler'], 
                                      swimming_pool = data['swimming_pool'])
            # store profile in db
            profile.save()
            # go to results page
            return HttpResponseRedirect('/done/')
            return HttpResponseRedirect(reverse('evaluation_result', username=data['username']))
    else:
        form = EvaluatorForm()

    context = {
        'form': form
    }
    return render(request, 'evaluate.html', context=context)


def evaluate_js(request):
    form = EvaluatorForm()
    context = {'form': form}
    return render(request, 'evaluate.js', context=context, content_type='text/javascript')

def result(request):
    return render(request, 'results.html')