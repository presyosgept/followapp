from rest_framework import serializers
from .models import Counselor, Faculty

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