from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from answer import views

answer_router = routers.DefaultRouter()
answer_router.register('',views.answerViewSet)

urlpatterns = [
    path('answers/',include(answer_router))
]