from rest_framework import serializers
from .model import questions

class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = questions
        fields = '__all__'