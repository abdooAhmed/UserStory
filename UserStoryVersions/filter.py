import django_filters
from django import forms
from UserStoryApp.models import UserStoryVersion


class userStoryVersionsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search place', 'class': 'form-control'}))
    description = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search place', 'class': 'form-control'}))

    class Meta:
        model = UserStoryVersion
        fields = ['name', 'description']
