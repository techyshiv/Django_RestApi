from django.shortcuts import render
# from rest_framework.response import Response
# Create your views here.
# function based api view
# from rest_framework.decorators import api_view
# @api_view()
# def hello_world(request):
#     return Response({'msg':'Hello World!'})

# or
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'Get Request!'})
# @api_view(['POST'])
# def hello_world(request):
#     if request.method=="POST":
#         print(request.data)
#         return Response({'msg':'Post Request!'})

# Use get and post together

# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method=="GET":
#         return Response({"msg":"This is Get Request"})
#     if request.method=="POST":
#         print(request.data)
#         return Response({'msg':'Post Request!'})

# Create Crud Opeartion with api view and Browsable api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# For third party application
# @api_view(["GET","POST","PUT","DELETE"])
# def student_api(request):
#     if request.method=="GET":
#         id=request.data.get("id")
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return Response(serializer.data)

#     if request.method == "POST":
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Msg":"Data Created"})
#         return Response(serializer.errors)

#     if request.method=="PUT":
#         id = request.data.get("id")
#         stu=Student.objects.get(pk=id)
#         serializer=StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Msg":"Data Updated"})
#         else:
#             return Response(serializer.errors)

#     if request.method == "DELETE":
#         id = request.data.get("id")
#         stu=Student.objects.get(pk=id)
#         stu.delete()
#         return Response({"Msg":"Data Deleted"})
# for browsable api

@api_view(["GET","POST","PUT","PATCH","DELETE"])
def student_api(request,pk=None):
    if request.method=="GET":
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg":"Data Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    if request.method=="PUT":
        id = pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg":"Data Completely Updated"})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=="PATCH":
        id = pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg":"Data Partially Updated"})
        else:
            return Response(serializer.errors)

    if request.method == "DELETE":
        id = pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({"Msg":"Data Deleted"})

