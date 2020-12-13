# Concrete View class in Django Rest Framework
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView

# One by One
# class StudentListAPI(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentCreateAPI(CreateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentRetriveAPI(RetrieveAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentUpdateAPI(UpdateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentDeleteAPI(DestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# Group all together
class LCStudentAPI(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class RUDStudentAPI(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer