from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.urls import reverse
from evaluator.forms import EvaluatorForm
from user_profile.models import UserProfile


@login_required
def evaluate(request):
    if request.method == 'POST':
        # get form data from post
        form = EvaluatorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # if profile with given username already exists, update profile. 
            # otherwise make profile for user
            try:
                profile = UserProfile.objects.get(user=request.user)
                profile.weekly_laundry_loads = data['weekly_laundry_loads']
                profile.washer_type = data['washer_type']
                profile.daily_bathroom_trips = data['daily_bathroom_trips']
                profile.weekly_showers = data['weekly_showers']
                profile.shower_head = data['shower_head']
                profile.shower_times = data['shower_times']
                profile.weekly_baths = data['weekly_baths']
                profile.weekly_dishes = data['weekly_dishes']
                profile.weekly_sprinkler = data['weekly_sprinkler']
                profile.swimming_pool = data['swimming_pool']
            except UserProfile.DoesNotExist:
                profile = UserProfile(user=request.user, weekly_laundry_loads = data['weekly_laundry_loads'],
                                      washer_type=data['washer_type'], 
                                      daily_bathroom_trips = data['daily_bathroom_trips'],
                                      weekly_showers = data['weekly_showers'], 
                                      shower_times = data['shower_times'], 
                                      shower_head=data['shower_head'], 
                                      weekly_baths = data['weekly_baths'], 
                                      weekly_dishes = data['weekly_dishes'], 
                                      weekly_sprinkler = data['weekly_sprinkler'], 
                                      swimming_pool = data['swimming_pool'])
            # store profile in db
            profile.save()
            return HttpResponse(request, 'Success!')

    # send html on non-POST requests
    return render(request, 'evaluate.html')


def evaluate_js(request):
    return render(request, 'evaluate.js', content_type='text/javascript')
