from django import forms
from UserStoryApp.models import Role


class AddUserForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField()
    Role = forms.TypedChoiceField(choices=[(choice.value, choice.name)
                                           for choice in Role], widget=forms.Select(attrs={'class': 'form-control form-select'}))
