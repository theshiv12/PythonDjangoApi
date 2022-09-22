from django.urls import path
from employee import api
urlpatterns = [
        path('api/<int:pk>',api.single_employe_crud),        
        # path('api/create',EmployeeCreateApi.as_view()),
        # path('api/update/<int:pk>',EmployeeCreateApi.as_view()),
        # path('api/delete/<int:pk>',EmployeeCreateApi.as_view())

]