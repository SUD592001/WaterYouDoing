from django import forms


shower_head_choices = [
    ("normal", "Normal shower head"),
    ("efficient", "Efficient shower head"),
]

washer_type_choices = [
    ("top", "Top-load washer"),
    ("front", "Front-load washer"),
]

swimming_pool_choices = [
    ("none", "No pool"),
    ("small", "Small pool"),
    ("medium", "Medium pool"),
    ("large", "Large pool"),
]

class EvaluatorForm(forms.Form):
    weekly_laundry_loads = forms.IntegerField(required=True)
    washer_type = forms.ChoiceField(required=True, choices=washer_type_choices)
    daily_bathroom_trips = forms.IntegerField(required=True)
    weekly_showers = forms.IntegerField(required=True)
    shower_head = forms.ChoiceField(required=True, choices=shower_head_choices)
    shower_times = forms.IntegerField(required=True)
    weekly_baths = forms.IntegerField(required=True)
    weekly_dishes = forms.IntegerField(required=True)
    weekly_sprinkler = forms.IntegerField(required=True)
    swimming_pool = forms.ChoiceField(required=True, choices=swimming_pool_choices)
