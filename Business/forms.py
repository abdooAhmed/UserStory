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
    businessIndustry = MyModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        queryset=BusinessCategory.objects.all()
    )
    hourlyRate = forms.IntegerField()
    # LegalEntityName = forms.CharField()
    # Address = forms.CharField()
    # BusinessNumber = forms.IntegerField()
    # BusinessEmail = forms.CharField()
    Internal_User = UserMyModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        queryset=User.objects.filter(Role=2)
    )
    Customer = UserMyModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        queryset=User.objects.filter(Role=1)
    )


class AddBusinessForm2(forms.Form):
    LegalEntityName = forms.CharField(required=False)
    Address = forms.CharField(required=False)
    BusinessNumber = forms.IntegerField(required=False)
    BusinessEmail = forms.CharField(required=False)
    ABN = forms.IntegerField(required=False)
