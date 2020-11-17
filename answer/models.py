from django.db import models
from question.models import questions

class answers(models.Model):
    a_content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    question  = models.ForeignKey(questions, on_delete=models.CASCADE)