from django.contrib import admin
from .models import BranchModel,EmployeeModel,EmpDetailsModel

# Register your models here.
admin.site.register(BranchModel)
admin.site.register(EmployeeModel)
admin.site.register(EmpDetailsModel)


