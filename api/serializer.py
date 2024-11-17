from rest_framework import serializers
from .models import *

class studentserial(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=20)

    def create(self, validated_data):#when you create data
        return data.objects.create(**validated_data)

    def update(self,instance, validated_data):# when you update data
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance

# ek toh uper ka code likhiye ya fir niche wala dono same kaam karenge
# isme create, update methods banane ki koi jarurat nahi hai
class studentserial(serializers.ModelSerializer):
    class Meta:
        model = data
        fields =['name','roll','city']