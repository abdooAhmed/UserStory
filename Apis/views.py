from UserStoryApp.models import UserStory
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.


def del_userStroy(request, id):
    print(id)
    instance = UserStory.objects.get(id=id)
    instance.delete()
    return JsonResponse({"dc": id}, safe=False)
