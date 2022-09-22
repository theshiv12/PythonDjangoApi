# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import permissions
# from .models import Employee
# from .serializer import EmployeeSerializer

# class ProjectAPIView(APIView):
#   permission_classes = [permissions.AllowAny]

#   def get(self,request,*args,**kwargs):
#     projects = Employee.objects.all()
#     serializer = EmployeeSerializer(projects, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
  
#   def post(self, request, *args, **kwargs):
#     data = {
#         'title': request.data.get('title'), 
#         'description': request.data.get('description'), 
#     }
#     serializer = EmployeeSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProjectDetailAPIView(APIView):
#   permission_classes = [permissions.AllowAny]

#   def delete(self, request, id, *args, **kwargs):
#       if Employee.objects.filter(id=id).exists():
#         Employee = Employee.objects.get(id=id)
#         Employee.delete()
#         return Response({"response":"Employee Deleted"}, status=status.HTTP_200_OK)
#       else:
#           return Response(
#               {"res": "Employee Doesn't Exists"},
#               status=status.HTTP_400_BAD_REQUEST
#           )

#   def patch(self, request, id, *args, **kwargs):
#     if Employee.objects.filter(id=id).exists():
#       employee = Employee.objects.get(id=id)
#       data = {
#       'title': request.data.get('title'), 
#       'description': request.data.get('description'), 
#       }
#       serializer = EmployeeSerializer(instance = employee, data=data, partial = True)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data, status=status.HTTP_200_OK)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response(
#                 {"res": "Project Doesn't Exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
