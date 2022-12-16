from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.


def get(self, request, *args, **kwargs):
    return Response({"dc": "dc"}, status=status.HTTP_200_OK)
