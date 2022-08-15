from rest_framework import generics,viewsets,status
from rest_framework.views import APIView
from django import views
from rest_framework.response import Response
from api.models import EmployeeDBModel,BranchModel,EmployeeModel,EmpDetailsModel
from api.serializers import EmployeeDBSerializer,BranchSerializer,EmployeeSerializer,EmpDetailsSerializer,BranchNestedSerializer,EmployeeNestedSerializer,EmpDetailsNestedSerializer,EmployeeUpdateSerializer,EmpDetailsUpdateSerializer

# Create your views here.
# ------------------CRUD---------------------
class EmployeeDBListCreateAPI(generics.ListCreateAPIView):
    queryset=EmployeeDBModel.objects.all()
    serializer_class=EmployeeDBSerializer

# ------------------Create, list details---------------------
class BranchListCreateAPI(generics.ListCreateAPIView):
    queryset=BranchModel.objects.all()
    serializer_class=BranchSerializer

class ListEmployees(generics.ListCreateAPIView):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer

class ListEmployeeById(APIView):
    def get(self,request,id):
        name=EmployeeModel.objects.filter(branch=id)
        serializer=EmployeeSerializer(name,many=True)
        return Response(serializer.data)

class ListEmployeeDetails(generics.ListCreateAPIView):
    queryset=EmpDetailsModel.objects.all()
    serializer_class=EmpDetailsSerializer

class ListDetailsById(APIView):
    def get(self,request,id):
        name=EmpDetailsModel.objects.filter(id=id)
        serializer=EmpDetailsSerializer(name,many=True)
        return Response(serializer.data)

# ------------------Nested view---------------------
# class EmpDetailsNestedListCreateAPI(generics.ListCreateAPIView):
#     queryset=EmpDetailsModel.objects.all()
#     serializer_class=BranchNestedSerializer

# class EmpDetailsNestedListCreateAPI(generics.ListCreateAPIView):
#     queryset=EmpDetailsModel.objects.all()
#     serializer_class=EmployeeNestedSerializer

class EmpDetailsNestedListCreateAPI(generics.ListCreateAPIView):
    queryset=EmpDetailsModel.objects.all()
    serializer_class=EmpDetailsNestedSerializer

class EmpDetailsNestedListViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=EmpDetailsModel.objects.all()
    serializer_class=EmpDetailsNestedSerializer

# ----------------------update,delete Details(non-nested)----------------

class EmployeeDBListViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=EmployeeDBModel.objects.all()
    serializer_class=EmployeeDBSerializer



class EmployeeListViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer


# ---------update,delete without id-----------

class EmployeeUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeUpdateSerializer

class EmpDetailsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=EmpDetailsModel.objects.all()
    serializer_class=EmpDetailsUpdateSerializer

class BranchListViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=BranchModel.objects.all()
    serializer_class=BranchSerializer


# class EmpDetailsListViewUpdateDelete(APIView):
#     def get_delete_update_puppy(self,request,id):
#         try:
#             name = EmployeeModel.objects.filter(id=id)
#         except EmployeeModel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
            
#         if request.method == 'GET':
#             serializer = EmpDetailsSerializer(name,many=True)
#             return Response(serializer.data)
        
#         if request.method == 'PUT':
#             serializer = EmpDetailsSerializer(name, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    


    # queryset=EmpDetailsModel.objects.all()
    # serializer_class=EmpDetailsNestedSerializer
    
    # def put(self,request,id,format=None):
    #     post=EmpDetailsModel.objects.get(id=id)
    #     post.put()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
