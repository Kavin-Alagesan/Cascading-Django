from django.urls import path
from api import views

urlpatterns=[
    path('api/',views.EmployeeDBListCreateAPI.as_view()),
    path('api/<int:pk>/',views.EmployeeDBListViewUpdateDelete.as_view()),
    path('branch/',views.BranchListCreateAPI.as_view()),
    path('branch/<int:pk>/',views.BranchListViewUpdateDelete.as_view()),

    path('employee_list/',views.ListEmployees.as_view()),
    path('employee/<int:id>/',views.ListEmployeeById.as_view()),
    path('nested_employee/<int:pk>/',views.EmployeeListViewUpdateDelete.as_view()),

    path('emp_details_list/',views.ListEmployeeDetails.as_view()),
    path('nested_emp_details_list/',views.EmpDetailsNestedListCreateAPI.as_view()),
    path('emp_details/<int:id>/',views.ListDetailsById.as_view()),

    path('employee_put_delete/<int:pk>/',views.EmployeeUpdateDelete.as_view()),
    path('emp_details_put_delete/<int:pk>/',views.EmpDetailsUpdateDelete.as_view()),

    path('nested_emp_details/<int:pk>/',views.EmpDetailsNestedListViewUpdateDelete.as_view()),
]
