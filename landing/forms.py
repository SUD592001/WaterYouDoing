from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(UserCreationForm):
    email = forms.EmailField(label='Email address', required=True)
    bio = forms.CharField(required=False, widget=forms.Textarea)

    def clean(self):
        data = super().clean()
        # email has to be unique
        try:
            user = User.objects.get(email=data["email"])
            raise ValidationError("Email address has already been registered!")
        except User.DoesNotExist:
            pass
