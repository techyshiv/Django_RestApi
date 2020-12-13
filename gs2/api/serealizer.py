from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    class Meta:
        model = Student
        fields = '__all__'

def create(self,validate_data):
    return Student.objects.create(**validate_data)