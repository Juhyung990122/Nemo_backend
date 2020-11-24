from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .serializers import answerSerializer
from .models import answers

class answerViewSet(viewsets.ModelViewSet):
    queryset = answers.objects.all()
    serializer_class = answerSerializer