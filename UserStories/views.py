from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from UserStoryApp.models import UserStory, Persona, DevelopmentTask, RAIDS, Epic, US_Group, UserStoryVersion, Project, Platform, Estimates
from .forms import AddUserStoryForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .filters import UserStoriesFilter
from json import dumps
# Create your views here.


@login_required
def userStories_list(request):
    personaObjects = list(Persona.objects.values_list('Name'))
    print(personaObjects)
    personaObjects = dumps(personaObjects)
    persona = ""
    RAIDS = ""
    DevTask = ""
    Indicator = ""
    userStories = UserStory.objects.all()
    my_filter = UserStoriesFilter(request.GET, queryset=userStories)
    userStories = my_filter.qs
    if request.GET.get("Persona"):
        userStories = userStories.filter(
            Persona__Name__contains=request.GET.get("Persona"))
        persona = request.GET.get("Persona")
    if request.GET.get("RAIDS"):
        userStories = userStories.filter(
            RAIDS__description__contains=request.GET.get("RAIDS"))
        RAIDS = request.GET.get("RAIDS")
    if request.GET.get("DevTask"):
        userStories = userStories.filter(
            DevelopmentTask__description__contains=request.GET.get("DevTask"))
        DevTask = request.GET.get("DevTask")
    if request.GET.get("Indicator"):
        userStories = userStories.filter(
            US_Group__description__contains=request.GET.get("Indicator"))
        Indicator = request.GET.get("Indicator")
    return render(request, 'userStories/userStories.html', {'users': userStories, 'filter': my_filter, 'personaObjects': personaObjects, 'form': {'persona': persona, 'RAIDS': RAIDS, 'DevTask': DevTask, 'indicator': Indicator}})


@login_required
@csrf_protect
def add_userStory(request):
    personaObjects = list(Persona.objects.values_list('Name'))
    print(personaObjects)
    personaObjects = dumps(personaObjects)
    epicObjects = list(Epic.objects.values_list('versionName'))
    epicObjects = dumps(epicObjects)
    platforms = Platform.objects.all()
    current_user = request.user
    print("dc")
    if request.method == 'GET' and 'Platform' in request.GET:
        print("here")
        Platform.objects.create(name=request.GET.get("Name"))
        print(request.GET.get("platform"))
        return redirect('/UserStories/addUserStory/')
    if request.method == 'POST':
        platformIds = request.POST.getlist("platforms")
        platformIds = [eval(i) for i in platformIds]
        noOfHoursList = request.POST.getlist("estimate[]")
        estimates = []
        for i in range(len(platformIds)):
            platformObject = Platform.objects.get(id=platformIds[i])
            print(platformObject)
            estimates.append(
                Estimates.objects.create(noOfHours=noOfHoursList[i], Platform=platformObject))
        uS_Group = US_Group.objects.create(
            description=request.POST.get("US_Group"))
        persona = []
        personas = request.POST.getlist("Persona")
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
        userStory = UserStory.objects.create(
            iWantTO=request.POST.get("IWantTO"),
            soThat=request.POST.get("SoThat"),
            Epic=epic,
            US_Group=uS_Group
        )
        userStory.Persona.set(persona)
        userStory.RAIDS.set(RaidsResult)
        userStory.DevelopmentTask.set(devResult)
        userStory.Estimates.set(estimates)
    return render(request, 'userStories/addUserStory.html', {'platforms': platforms, 'userName': current_user.username, 'personaObjects': personaObjects, 'epicObjects': epicObjects})


def userStoryDetails(request, id):
    User = get_user_model()
    users = UserStory.objects.get(id=id)
    return render(request, 'userStories/userStoryDetails.html', {'userStory': users})
