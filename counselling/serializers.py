from rest_framework import serializers
from .models import Counselor, Faculty

class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'