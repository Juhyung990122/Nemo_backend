from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from user import views

user_router = routers.DefaultRouter()
user_router.register('',views.userViewset)

urlpatterns = [
    path('users/',include(user_router.urls))
]