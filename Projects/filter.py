import django_filters
from django import forms
from UserStoryApp.models import Project


class ProjectsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search place', 'class': 'form-control filter'}))

    class Meta:
        model = Project
        fields = ['name']
