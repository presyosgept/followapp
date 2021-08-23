from rest_framework import serializers
from .models import Students,Counselor

class studentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class counselorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Counselor
        fields = '__all__'