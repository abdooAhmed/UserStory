from UserStoryApp.models import UserStory, Persona
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from json import dumps
# Create your views here.


def del_userStroy(request, id):
    print(id)
    instance = UserStory.objects.get(id=id)
    instance.delete()
    return JsonResponse({"dc": id}, safe=False)


def related_userStory(request):
    dataObject = []
    print(type(dataObject))
    persona = request.GET.get("Persona")
    epic = request.GET.get("Epic")

    if bool(persona.strip()):
        userStories = UserStory.objects.filter(
            Persona__Name__contains=persona)
        print(len(userStories))
    if bool(epic.strip()):
        userStories = userStories.filter(
            Epic__versionName__contains=epic)
        print(len(userStories))
    print(len(userStories))
    for userStory in userStories.all():
        iWantTO = userStory.iWantTO
        soThat = userStory.soThat
        priority = userStory.priority
        id = userStory.id
        personaObject = []
        [personaObject.append(i.Name) for i in userStory.Persona.all()]
        RAIDS = []
        [RAIDS.append(i.description) for i in userStory.RAIDS.all()]
        DevelopmentTask = []
        [DevelopmentTask.append(i.description)
         for i in userStory.DevelopmentTask.all()]
        epicObject = userStory.Epic.versionName
        dataObject.append(
            {'iWantTO': iWantTO, 'soThat': soThat, 'priority': priority, 'id': id, 'persona': personaObject,
             'RAIDS': RAIDS, 'devTask': DevelopmentTask, 'epic': epicObject})
    dataObject = dumps(dataObject)
    return JsonResponse(dataObject, safe=False)
