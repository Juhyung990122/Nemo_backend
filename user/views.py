from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .serailizer import userSerializer
from .model import users

class userViewSets(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = userSerializer
    