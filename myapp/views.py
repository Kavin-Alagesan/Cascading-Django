from django.contrib import messages
from django.shortcuts import redirect, render
import requests
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'base.html')

def get_branch(request):
    if request.method=='POST':
        print('------------Create branch-------')
        branch=request.POST['txtBranch']
        data={
            'branch':branch,
        }
        url="http://127.0.0.1:8000/api/branch/"
        response=requests.post(url,data=data)
        messages.success(request,("Branch created successfully"))
        return redirect('get_emp_name')
    url="http://127.0.0.1:8000/api/branch/"
    response=requests.get(url).json()
    print("------------Branch Refresh-----------")
    return render(request,'emp_details/get_emp_name.html',{'response':response})

    return render(request,'emp_details/get_branch.html',{'response':response})

def get_emp_name(request):
    if request.method=='POST':
        print('------------Create Name-------')
        branch=request.POST['selectBranch']
        emp_name=request.POST['txtEmp_name']
        emp_id=request.POST['txtEmp_id']
        data={
            'branch':branch,
            'emp_name':emp_name,
            'emp_id':emp_id,
        }
        url="http://127.0.0.1:8000/api/employee_list/"
        response=requests.post(url,data=data)
        messages.success(request,("Employee created successfully"))
        return redirect('get_emp_details')
    url="http://127.0.0.1:8000/api/branch/"
    response=requests.get(url).json()
    print("------------Emp Refresh-----------")
    return render(request,'emp_details/get_emp_name.html',{'response':response})

def get_emp_details(request):
    if request.method=='POST':
        print('------------Create emp details-------')
        branch=request.POST['selectBranch']
        emp_name=request.POST['selectEmp_name']
        emp_fullname=request.POST['txtFullname']
        gender=request.POST['radioGender']
        blood_group=request.POST['selectBlood_group']
        dob=request.POST['dateDOB']
        designation=request.POST['txtDesignation']
        contact_number=request.POST['txtContact_number']
        photo=request.FILES.get('filePhoto')
        data={
            'branch':branch,
            'emp_name':emp_name,
            'emp_fullname':emp_fullname,
            'gender':gender,
            'blood_group':blood_group,
            'dob':dob,
            'designation':designation,
            'contact_number':contact_number,
        }
        file={
            'photo':photo
        }
        url="http://127.0.0.1:8000/api/emp_details_list/"
        response=requests.post(url,data=data,files=file)
        print(response.text)
        messages.success(request,("Employee details added successfully"))
        return redirect('list_details')
    url="http://127.0.0.1:8000/api/branch/"
    response=requests.get(url).json()
    print("------------Refresh-----------")
    return render(request,'emp_details/get_emp_details.html',{'response':response})

def list_details(request):
    print('------------List details-------')
    url="http://127.0.0.1:8000/api/nested_emp_details_list/"
    response=requests.get(url).json()
    key = requests.get('http://127.0.0.1:8000/api/branch/').json()
    return render(request,'emp_details/list_details.html',{'response':response, 'key' : key})

def update(request,id):
    if request.method=='POST':
        print('------------update emp details-------')
        emp_fullname=request.POST['txtFullname']
        gender=request.POST['radioGender']
        blood_group=request.POST['selectBlood_group']
        dob=request.POST['dateDOB']
        designation=request.POST['txtDesignation']
        contact_number=request.POST['txtContact_number']
        photo=request.FILES.get('filePhoto')
        data={
            'emp_fullname':emp_fullname,
            'gender':gender,
            'blood_group':blood_group,
            'dob':dob,
            'designation':designation,
            'contact_number':contact_number,
        }
        file={
            'photo':photo
        }

        branch=request.POST['selectBranch']
        data_branch={
            'branch':branch,
        }

        emp_name=request.POST['selectEmp_name']
        data_emp_name={
            'emp_name':emp_name,
        }

        print(data)
        print(data_branch)
        print(data_emp_name)

        branch_id=request.POST['branch_id']
        employee_id=request.POST['employee_id']
        details_id=request.POST['details_id']

        url="http://127.0.0.1:8000/api/branch/{id}/"
        a=requests.put(url.format(id=branch_id),data=data_branch)

        url="http://127.0.0.1:8000/api/employee_put_delete/{id}/"
        b=requests.put(url.format(id=employee_id),data=data_emp_name)

        url="http://127.0.0.1:8000/api/emp_details_put_delete/{id}/"
        response=requests.put(url.format(id=details_id),data=data,files=file)
        print(a)
        print(b)
        print(response)

        messages.success(request,("Employee details updated successfully"))
        return redirect('list_details')
    url="http://127.0.0.1:8000/api/nested_emp_details_list/"
    response=requests.get(url).json()
    print('------------------refresh edit-------------------------')
    print(response.text)
    return render(request,'emp_details/list_details.html',{'response':response})

def delete(request,id):
    response=requests.delete("http://127.0.0.1:8000/api/emp_details_put_delete/{id}/".format(id=id))
    messages.success(request,("Details deleted successfully"))
    url="http://127.0.0.1:8000/api/nested_emp_details_list/"
    response=requests.get(url).json()
    return render(request,'emp_details/list_details.html',{'response':response})
