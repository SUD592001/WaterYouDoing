from django import forms


class EvaluatorForm(forms.Form):
    weekly_laundry_loads = forms.IntegerField(label='On average, how many loads of laundry do you use ' +
                                                    'per week?', required=True)

    daily_bathroom_trips = forms.IntegerField(label='On average, how many times do you go to the bathroom each day? ', 
                                                    required=True)

    weekly_showers = forms.IntegerField(label='On average, how many showers do you take in a week? ', required=True)

    shower_times = forms.IntegerField(label='On average, how long are your showers? (in minutes) ', required=True)

    weekly_baths = forms.IntegerField(label='On average, how many baths do you take in a week? ', required=True)

    weekly_dishes = forms.IntegerField(label='On average, how many times do you wash your dishes in a week? ', 
                                                    required=True)

    weekly_sprinkler = forms.IntegerField(label='On average, how many times do you water your lawn in a week? ', 
                                                    required=True)

    swimming_pool = forms.IntegerField(label='Do you have a swimming pool? ',  required=True)

    username = forms.CharField(label='Username', min_length=4, max_length=30, required=True)
