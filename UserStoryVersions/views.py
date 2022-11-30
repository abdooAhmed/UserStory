from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from UserStoryApp.models import UserStoryVersion
from .forms import AddUserStoryVersionForm
from django.contrib.auth.decorators import login_required
from .filter import userStoryVersionsFilter
# Create your views here.


@login_required
def userStoryVersions_list(request):
    PROJECT = ""
    CREATOR = ""
    userStoriesVersions = UserStoryVersion.objects.all()
    my_filter = userStoryVersionsFilter(
        request.GET, queryset=userStoriesVersions)
    userStoriesVersions = my_filter.qs
    if request.GET.get("PROJECT"):
        userStoriesVersions = userStoriesVersions.filter(
            Project__name__contains=request.GET.get("PROJECT"))
        PROJECT = request.GET.get("PROJECT")
    if request.GET.get("CREATOR"):
        userStoriesVersions = userStoriesVersions.filter(
            User__username__contains=request.GET.get("CREATOR"))
        CREATOR = request.GET.get("CREATOR")
    return render(request, 'userStoryVersions/userStoryVersions.html', {'users': userStoriesVersions, 'filter': my_filter, 'form': {'PROJECT': PROJECT, 'CREATOR': CREATOR}})


@login_required
def add_userStoryVersions(request):
    if request.method == 'POST':
        print('done')
        form = AddUserStoryVersionForm(request.POST)
        if form.is_valid():
            current_user = request.user
            cd = form.cleaned_data
            user = UserStoryVersion.objects.create(
                name=cd['name'], description=cd['description'], Project=cd['projects'], User=current_user)
            if user is not None:
                return redirect('/UserStoryVersion/list/')
    else:
        form = AddUserStoryVersionForm()
    print(form)
    return render(request, 'userStoryVersions/addUserStoryVersion.html', {'form': form})
