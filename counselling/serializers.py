from rest_framework import serializers
from .models import Counselor, Faculty
from django.contrib.auth.forms import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class Result(object):
    def __init__(self, bool1):
        self.result = bool1
  
# create a serializer
class ResultSerializer(serializers.Serializer):
    # intialize fields
    result = serializers.BooleanField()