from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .serializers import questionSerializer
from .models import questions

class questionViewSet(viewsets.ModelViewSet):
    queryset = questions.objects.all()
    serializer_class = questionSerializer