from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from UserStoryApp.models import UserStory, Persona, DevelopmentTask, RAIDS, Category, Epic, US_Group
from .forms import AddUserStoryForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .filters import UserStoriesFilter
# Create your views here.


@login_required
def userStories_list(request):
    Persona = ""
    RAIDS = ""
    DevTask = ""
    Indicator = ""
    userStories = UserStory.objects.all()
    my_filter = UserStoriesFilter(request.GET, queryset=userStories)
    userStories = my_filter.qs
    if request.GET.get("Persona"):
        userStories = userStories.filter(
            Persona__Name__contains=request.GET.get("Persona"))
        Persona = request.GET.get("Persona")
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
    return render(request, 'userStories/userStories.html', {'users': userStories, 'filter': my_filter, 'form': {'persona': Persona, 'RAIDS': RAIDS, 'DevTask': DevTask}})


@login_required
@csrf_protect
def add_userStory(request):
    if request.method == 'POST':
        uS_Group = US_Group.objects.create(
            description=request.POST.get("US_Group"))
        persona = []
        persona.append(Persona.objects.create(
            Name=request.POST.get("Persona")))
        print(request.POST.get("Dev"))
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
        epicCategory = []
        epicCategory.append(Category.objects.create(
            name=request.POST.get("EpicCategory")))
        epic = Epic.objects.create(
            versionName=request.POST.get("Epic"))
        epic.Category.set(epicCategory)
        userStory = UserStory.objects.create(
            iWantTO=request.POST.get("IWantTO"),
            soThat=request.POST.get("SoThat"),
            priority=request.POST.get("Priority"),
            Epic=epic,
            US_Group=uS_Group
        )
        userStory.Persona.set(persona)
        userStory.RAIDS.set(RaidsResult)
        userStory.DevelopmentTask.set(devResult)
    return render(request, 'userStories/addUserStory.html')


def userDetails(request, id):
    User = get_user_model()
    users = User.objects.get(id=id)
    return render(request, 'user/userDetails.html', {'user': users})
