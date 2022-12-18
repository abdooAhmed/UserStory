import django_filters
from django import forms
from UserStoryApp.models import UserStory


class UserStoriesFilter(django_filters.FilterSet):
    iWantTO = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search place', 'class': 'form-control filter'}))
    soThat = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search place', 'class': 'form-control filter'}))

    class Meta:
        model = UserStory
        fields = ['iWantTO', 'soThat', 'priority']
