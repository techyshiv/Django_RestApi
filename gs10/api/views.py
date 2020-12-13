from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# Model View set
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# Model ReadOnly View set
# class StudentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer