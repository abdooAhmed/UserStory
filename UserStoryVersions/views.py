from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from UserStoryApp.models import UserStory, Persona, DevelopmentTask, RAIDS, Epic, US_Group, UserStoryVersion, Project, Business
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
    if request.method == 'POST':
        uS_Group = US_Group.objects.create(
            description=request.POST.get("US_Group"))
        persona = []
        personas = request.POST.get("Persona").splitlines()
        for p in personas:
            persona.append(Persona.objects.create(
                Name=request.POST.get("Persona")))
        devs = request.POST.get("Dev").splitlines()
        devResult = []
        for dev in devs:
            devResult.append(DevelopmentTask.objects.create(description=dev))
        # estimates = request.POST.get("Estimates").splitlines()
        # for estimate in estimates:
        #     Estimates.objects.create()
        Raids = request.POST.get("RAIDS").splitlines()
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
            US_Group=uS_Group,
            userStoriesVersion=userStoryVersion
        )
        userStory.Persona.set(persona)
        userStory.RAIDS.set(RaidsResult)
        userStory.DevelopmentTask.set(devResult)
        userStories.append(userStory)
        if not request.POST.get('AddAnother'):
            print(request.POST.get('AddAnother'))
            return redirect('/UserStoryVersion/list/', {'persona': persona, 'userStories': userStories})
        business = Business.objects.all()
        projects = Project.objects.all()
        return render(request, 'userStoryVersions/addUserStoryVersion.html', {'persona': projects, 'userStories': userStories, 'userStoryVersion': userStoryVersion, 'business': business})
    project = Project.objects.all()
    business = Business.objects.all()
    projects = []
    for p in project:
        projects.append({'id': p.id, 'name': p.name,
                        'business': p.Business.id})
    projectJson = dumps(projects)
    return render(request, 'userStoryVersions/addUserStoryVersion.html', {'persona': projects, 'project': projectJson, 'userStories': userStories, 'business': business})


def userStoryVersionDetails(request, id):
    User = get_user_model()
    userStoryVersion = UserStoryVersion.objects.get(id=id)
    userStory = UserStory.objects.filter(
        userStoriesVersion=userStoryVersion)
    projects = Project.objects.all()
    print(userStoryVersion)
    print(userStory)
    return render(request, 'userStoryVersions/userStoryVersionsDetails.html',
                  {'userStoryVersion': userStoryVersion, 'userStories': userStory, 'persona': projects})
