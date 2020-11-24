from user import users
from rest_framework import serializers

class userSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        