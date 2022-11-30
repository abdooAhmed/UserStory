from django import forms


class AddUserForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField()
    Role = forms.CharField()
