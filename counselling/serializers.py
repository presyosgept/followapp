from rest_framework import serializers
from .models import Counselor

class counselorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Counselor
        fields = '__all__'