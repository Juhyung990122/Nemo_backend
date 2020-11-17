from django.db import models
from django.contrib.auth.models import AbstractUser

class users(AbstractUser):
    nickname = models.CharField(max_length=40)
    introduce = models.TextField()
    #MYSQL로 바꾸면서 ListField 로 갈아탈 예정
    following = models.TextField()
    follower = models.TextField()
    question = models.TextField()
    give_list = models.TextField()
    take_list = models.TextField()