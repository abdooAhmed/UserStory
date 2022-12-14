from django import forms
from UserStoryApp.models import BusinessCategory, Business, User


class MyModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class UserMyModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.username


class AddBusinessForm1(forms.Form):
    name = forms.CharField()
    hourlyRate = forms.IntegerField()
    # LegalEntityName = forms.CharField()
    # Address = forms.CharField()
    # BusinessNumber = forms.IntegerField()
    # BusinessEmail = forms.CharField()


class AddBusinessForm2(forms.Form):
    LegalEntityName = forms.CharField(required=False)
    Address = forms.CharField(required=False)
    BusinessNumber = forms.IntegerField(required=False)
    BusinessEmail = forms.CharField(required=False)
    ABN = forms.IntegerField(required=False)
