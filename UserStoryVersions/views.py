from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from UserStoryApp.models import UserStory, Persona, DevelopmentTask, Estimates, Platform, RAIDS, Epic, US_Group, UserStoryVersion, Project, Business
from .forms import AddUserStoryVersionForm
from django.contrib.auth.decorators import login_required
from .filter import userStoryVersionsFilter
from json import dumps
# Create your views here.

userStories = []


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
    print("here")
    userStoriesObjects = UserStory.objects.all()
    if request.method == 'GET' and 'Platform' in request.GET:
        Platform.objects.create(name=request.GET.get("Name"))
        print(request.GET.get("platform"))
        return redirect('/UserStoryVersion/addUserStoryVersion/')
    platforms = Platform.objects.all()
    if request.method == 'POST' and request.POST.get("project") != '0':
        persona = []
        platformIds = request.POST.getlist("platforms")
        platformIds = [eval(i) for i in platformIds]
        noOfHoursList = request.POST.getlist("estimate[]")
        estimates = []
        for i in range(len(platformIds)):
            platformObject = Platform.objects.get(id=platformIds[i])
            print(platformObject)
            estimates.append(
                Estimates.objects.create(noOfHours=noOfHoursList[i], Platform=platformObject))
        personas = request.POST.getlist("Persona")
        print(personas)
        for p in personas:
            persona.append(Persona.objects.create(
                Name=p))
        devs = request.POST.getlist("Dev")
        devResult = []
        for dev in devs:
            devResult.append(DevelopmentTask.objects.create(description=dev))
        # estimates = request.POST.get("Estimates").splitlines()
        # for estimate in estimates:
        #     Estimates.objects.create()
        Raids = request.POST.getlist("RAIDS")
        RaidsResult = []
        for Raid in Raids:
            RaidsResult.append(RAIDS.objects.create(description=Raid))
        epic = Epic.objects.create(
            versionName=request.POST.get("Epic"))
        current_user = request.user
        project_id = request.POST.get("project")
        project = Project.objects.get(id=request.POST.get("project"))
        VersionName = request.POST.get("VersionName")
        VersionDescription = request.POST.get("VersionDescription")
        userStoryVersion = UserStoryVersion.objects.create(
            name=VersionName, description=VersionDescription, Project=project, User=current_user)
        userStory = UserStory.objects.create(
            iWantTO=request.POST.get("IWantTO"),
            soThat=request.POST.get("SoThat"),
            priority=request.POST.get("Priority"),
            Epic=epic,
            userStoriesVersion=userStoryVersion,
        )
        userStory.Persona.set(persona)
        userStory.Estimates.set(estimates)
        print(RaidsResult)
        print(devResult)
        userStory.RAIDS.set(RaidsResult)
        userStory.DevelopmentTask.set(devResult)
        userStories.append(userStory)
        if not request.POST.get('AddAnother'):
            print("here")
            print(request.POST.get('AddAnother'))
            return redirect('/UserStoryVersion/list/', {'persona': persona, 'userStories': userStories})
        business = Business.objects.all()
        projects = Project.objects.all()
        print(userStories)
        return render(request, 'userStoryVersions/addUserStoryVersion.html', {'platforms': platforms, 'persona': projects, 'platformIds': platformIds, 'userStories': userStories, 'userStoryVersion': userStoryVersion, 'business': business})
    project = Project.objects.all()
    business = Business.objects.all()
    projects = []
    current_user = request.user
    for p in project:
        projects.append({'id': p.id, 'name': p.name,
                        'business': p.Business.id})
    projectJson = dumps(projects)
    del userStories[:]
    return render(request, 'userStoryVersions/addUserStoryVersion.html', {'platforms': platforms, 'persona': projects, 'userName': current_user.username, 'project': projectJson, 'business': business, 'userStoriesObject': userStoriesObjects})


def userStoryVersionDetails(request, id):
    User = get_user_model()
    userStoryVersion = UserStoryVersion.objects.get(id=id)
    userStory = UserStory.objects.filter(
        userStoriesVersion=userStoryVersion)
    project = Project.objects.all()
    business = Business.objects.all()
    projects = []
    current_user = request.user
    for p in project:
        projects.append({'id': p.id, 'name': p.name,
                        'business': p.Business.id})
    projectJson = dumps(projects)
    print(userStoryVersion.Project.name)
    return render(request, 'userStoryVersions/userStoryVersionsDetails.html',
                  {'userStoryVersion': userStoryVersion, 'userStories': userStory, 'persona': project, 'userName': current_user.username, 'project': projectJson, 'business': business})
