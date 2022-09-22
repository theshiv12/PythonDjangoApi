from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import EmployeeSerializer
from .models import Employee


@api_view(['GET','DELETE','POST'])
def single_employe_crud(request,pk):
    try:
        employe = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response()

    if request.method == 'GET':
         serializer = EmployeeSerializer(employe)
         return Response(serializer.data)

    elif request.method == 'PUT':
       data = EmployeeSerializer( employe,data=request.data)
       if data.is_valid():
            data.save()
            return Response(data.data)

    elif request.method == 'DELETE':
         employe.delete()
         return Response({"message":"deleted succesfully"})

    

@api_view(['GET','POST'])
def get_create_employe(request):
    if request.method=='POST':
        employe = EmployeeSerializer(data=request.data)
        if employe.is_valid():
            employe.save()
            return Response(employe.data)
        return Response(employe.errors)
    elif request.method=='GET':
        employe = Employee.objects.all()
        data =  EmployeeSerializer(employe,many=True)
        print(data.data)
        return Response(data.data)
   
# class EmployeeCreateApi(APIView):
    # def get(self , request,format=None):
    #      employe = Employee.objects.all()
    #      data =  EmployeeSerializer(employe,many=True)
    #      print(data.data)
    #      return Response(data.data)
    # def post(self, request, format=None):
    #     employe = EmployeeSerializer(data=request.data)
    #     if employe.is_valid():
    #         employe.save()
    #         return Response(employe.data)
    #     return Response(employe.errors)
    
    # def put(self , request,pk,format=None):
    #     employe = Employee.objects.get(pk=pk)
    #     data = EmployeeSerializer( employe,data=request.data)
    #     if data.is_valid():
    #         data.save()
    #         return Response(data.data)

    # def delete(self ,request,pk,format=None):
    #       employe = Employee.objects.get(pk=pk)
    #       employe.delete()
    #       return Response({"message":"deleted succesfully"})