from django import forms
from UserStoryApp.models import BusinessCategory, Business


class MyModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class AddProjectsForm(forms.ModelForm):
    hourlyRate = forms.IntegerField()
    name = forms.CharField()
    LegalEntityName = forms.CharField()
    Address = forms.CharField()
    BusinessNumber = forms.IntegerField()
    BusinessEmail = forms.CharField()
    businessIndustry = MyModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        queryset=BusinessCategory.objects.all()
    )

    class Meta:
        model = Business
        exclude = ['created_at', 'edited_at']
