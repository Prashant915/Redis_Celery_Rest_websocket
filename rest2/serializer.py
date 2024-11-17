from api.models import data
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= data
        fields = ['id','name','roll','city']