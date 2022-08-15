from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('get_branch/',views.get_branch,name='get_branch'),
    path('get_emp_name/',views.get_emp_name,name='get_emp_name'),
    path('get_emp_details/',views.get_emp_details,name='get_emp_details'),
    path('list_details/',views.list_details,name='list_details'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<id>/',views.delete,name='delete'),


]