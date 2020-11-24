from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

urlpatterns = [
    path('nemo-admin/', admin.site.urls),]
    path('user/',include('user.urls')),
    path('question/',include('question.urls')),
    path('answer/',include('answer.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
]
