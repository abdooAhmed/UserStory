from django import forms
from UserStoryApp.models import Business


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class AddProjectsForm(forms.Form):
    name = forms.CharField()
    status = forms.BooleanField(required=False)
    business = MyModelChoiceField(queryset=Business.objects.all())
