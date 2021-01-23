from django import forms


class EvaluatorForm(forms.Form):
    weekly_laundry_loads = forms.IntegerField(label='On average, how many loads of laundry do you use ' +
                                                    'per week?', required=True)
    username = forms.CharField(label='Username', min_length=4, max_length=30, required=True)
