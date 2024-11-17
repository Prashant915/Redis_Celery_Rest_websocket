from django.shortcuts import render
from .serializer import StudentSerializer
from api.models import data
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def studentapi(request,pk=None):
#     if request.method == 'GET':
#         # id= request.data.get('id') # request.data me sara data reheta hai
#         id=pk
#         if id is not None:
#             stu=data.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
        
#         stu= data.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)

#     if request.method == 'PUT':
#         id=pk
#         # id= request.data.get('id')
#         stu = data.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PATCH':
#         id=pk
#         # id= request.data.get('id')
#         stu = data.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'partial Data Updated'})
#         return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         id=pk
#         # id= request.data.get('id')
#         stu = data.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})
    

#class based APIView
#yaha pe api_view likhne ki koi jarurat nahi hai

class studentapi(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=data.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu= data.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
    
    def put(self,request,pk,format=None):
        id=pk
        # id= request.data.get('id')
        stu = data.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format=None):
        id=pk
        # id= request.data.get('id')
        stu = data.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial Data Updated'})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id=pk
        # id= request.data.get('id')
        stu = data.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
    

#Genereik API View Mixins
# ye bhi bilkul same kaam karega jaise uper waale krte hai

class StudentList(ListModelMixin,GenericAPIView):
    queryset=data.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
class StudentCreate(CreateModelMixin,GenericAPIView):
    queryset=data.objects.all()
    serializer_class=StudentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    

# you can do it in shortcut way as well for list and create
#do not need pk id
class StudentLC(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset=data.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    




class StudentRetrive(RetrieveModelMixin,GenericAPIView):
    queryset=data.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class StudentUpdate(UpdateModelMixin,GenericAPIView):# put ka kaam karega
    queryset=data.objects.all()
    serializer_class=StudentSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
class StudentDestroy(DestroyModelMixin,GenericAPIView):
    queryset=data.objects.all()
    serializer_class=StudentSerializer
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

# and similarly you can make shortcut of Retrive,Update and Destroy
# all three need pk id

class StudentRUD(RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin,GenericAPIView):
    queryset=data.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)