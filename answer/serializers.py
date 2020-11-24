from rest_framework import serializers
from .models import answers

class answerSerializer(serializers.ModelSerializer):
    class Meta:
        model = answers
        fields = '__all__'