from rest_framework import serializers
from .models import Counselor, Faculty
from django.contrib.auth.forms import User
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=User.objects.all(),
        #         fields=['username']
        #     )
        # ]

class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class Result(object):
    def __init__(self, bool1):
        self.result = bool1

class ResultSerializer(serializers.Serializer):
    result = serializers.BooleanField()

class Actor(object):
    def __init__(self, actor):
        self.actor = actor

class ActorSerializer(serializers.Serializer):
    actor = serializers.CharField(max_length=200)

