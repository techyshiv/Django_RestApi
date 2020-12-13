from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        # read only field apply on multiple
        # read_only_fields=["name","roll"]
        # extra_kwargs={'name':{'read_only':True}}

    # Field level validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError("Seat Full")
        return value
    # same as object level validation and validators