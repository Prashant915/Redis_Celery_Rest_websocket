from django.shortcuts import render
from .models import data 
from .serializer import studentserial
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# open myapp.py and run for the testing

#Model Object - Single Student Data
def student_detail(request,pk):
    stu=data.objects.get(id=pk) #here getting and writing numbers from urls
    serializer= studentserial(stu)
    json_data=JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)# safe=True is default parameter
    #for query set (fro all data)
    #stu=data.objects.all()
    #serializer=studentserial(stu,many=True)
    #then similar to model object
@csrf_exempt
def student_api(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=data.objects.get(id=id)
            serializer = studentserial(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=data.objects.all()
        serializer=studentserial(stu,many=True)
        json_data= JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == "POST":#proper deserializer example
        json_data = request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serializer= studentserial(data =pythondata)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"Data Created"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == "PUT":# updating partial data
        json_data = request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=data.objects.get(id=id)
        serializer= studentserial(stu,data =pythondata,partial=True)# if you dont want partial update remove "partial"
        if serializer.is_valid():
            serializer.save()
            res={"msg":"Data Updated"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == "DELETE":#deleting the data
        json_data = request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=data.objects.get(id=id)
        stu.delete()
        res={"msg":"Data Deleted"}
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=False)#uper ke 2 line ki jagah ye line bhi likh skte hai



#example of class based 
# @method_decorator(csrf_exempt, name='dispatch')
# class StudentAPI(View):
#     def get(self,request, *args, **kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id=pythondata.get('id',None)
#         if id is not None:
#             stu=data.objects.get(id=id)
#             serializer = studentserial(stu)
#             json_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         stu=data.objects.all()
#         serializer=studentserial(stu,many=True)
#         json_data= JSONRenderer().render(serializer.data)

#         return HttpResponse(json_data,content_type='application/json')
#     def post(self,request, *args, **kwargs):
#         json_data = request.body
#         stream= io.BytesIO(json_data)
#         pythondata= JSONParser().parse(stream)
#         serializer= studentserial(data =pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res={"msg":"Data Created"}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')

##similarly for put and delete also

##write URL like "path('studentapi/',views.StudentAPI.as_view())