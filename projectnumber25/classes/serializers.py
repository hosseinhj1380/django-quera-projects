from rest_framework import serializers
from .models import Classroom

class classrommserializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    capacity=serializers.IntegerField()
    department=serializers.CharField(max_length=50)
    area=serializers.DecimalField(max_digits=5, decimal_places=2)

    def validate(self, data):
        if data.get('capacity', 0) < 5 :
            error='Caparity must be more than or equal to 5.'

            raise serializers.ValidationError(error)
        if data.get('area', 0) < 0:
            error='Area must be positive value.'
            raise serializers.ValidationError(error)
        
        return data




