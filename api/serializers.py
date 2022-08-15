from rest_framework import serializers
from .models import EmployeeDBModel,BranchModel,EmployeeModel,EmpDetailsModel

# --------------------CRUD serializer---------------
class EmployeeDBSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeDBModel
        fields='__all__'

# ------------------List serializer(Nested)-------------
class BranchNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model=BranchModel
        fields=['id','branch']

class EmployeeNestedSerializer(serializers.ModelSerializer):
    branch=BranchNestedSerializer()
    class Meta:
        model=EmployeeModel
        fields=['id','branch','emp_name','emp_id']

class EmpDetailsNestedSerializer(serializers.ModelSerializer):
    emp_name=EmployeeNestedSerializer()
    class Meta:
        model=EmpDetailsModel
        fields=['id','emp_name','emp_fullname','gender','blood_group','dob','designation','contact_number','photo',]

# ------------------Create serializer-------------
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=BranchModel
        fields=['id','branch']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeModel
        fields=['id','branch','emp_name','emp_id']

class EmpDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmpDetailsModel
        fields=['id','emp_name','emp_fullname','gender','blood_group','dob','designation','contact_number','photo',]

# -----------------------for update details------------------
class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeModel
        fields=['id','emp_name']

class EmpDetailsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmpDetailsModel
        fields=['emp_fullname','gender','blood_group','dob','designation','contact_number','photo']


