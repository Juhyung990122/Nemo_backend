from django.db import models

class questions(models.Model):
    q_content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length = 200)
    STATE = (
        ('O','open'),
        ('C','close')
    )
    state = models.CharField(max_length=10, choices = STATE, default='O')
    #answer =
    CATEGORY = (
        ('A','anonymous'),
        ('N','named')
    )
    Category = models.CharField(max_length=20, choices=CATEGORY, default='N') 