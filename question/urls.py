from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from question import views

question_router = routers.DefaultRouter()
question_router.register('',views.questionViewSet)

urlpatterns = [
    path('questions/',include(question_router.urls))
]