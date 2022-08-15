from django.db import models

# Create your models here.

class EmployeeDBModel(models.Model):
    CHOICE_BRANCH=[
        ("Coimbatore","Coimbatore"),
        ("Bangalore","Bangalore"),
        ("Delhi","Delhi"),
    ] 
    CHOICE_GENDER=[
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    ]
    choices=CHOICE_BLOOD=[
        ('A-positive (A+)','A-positive (A+)'),
        ('A-negative (A-)','A-negative (A-)'),
        ('B-positive (B+)','B-positive (B+)'),
        ('B-negative (B-)','B-negative (B-)'),
        ('AB-positive (AB+)','AB-positive (AB+)'),
        ('AB-negative (AB-)','AB-negative (AB-)'),
        ('O-positive (O+)','O-positive (O+)'),
        ('O-negative (O-)','O-negative (O-)'),
    ]
    emp_no=models.AutoField(primary_key=True)
    branch=models.CharField(max_length=30,choices=CHOICE_BRANCH)
    emp_name=models.CharField(max_length=50)
    emp_fullname=models.CharField(max_length=75)
    gender=models.CharField(max_length=20,choices=CHOICE_GENDER)
    blood_group=models.CharField(max_length=20,choices=CHOICE_BLOOD)
    dob=models.DateField()
    designation=models.CharField(max_length=50)
    contact_number=models.PositiveIntegerField()
    photo=models.ImageField(upload_to='media/',blank=True)

    class Meta:
        db_table='EmployeeDBModel'

class BranchModel(models.Model):
    branch=models.CharField(max_length=30)
    
    def __str__(self):
        return self.branch

class EmployeeModel(models.Model):
    branch=models.ForeignKey(BranchModel,on_delete=models.CASCADE)
    emp_name=models.CharField(max_length=50)
    emp_id=models.SmallIntegerField()

    def __str__(self):
        return self.emp_name

class EmpDetailsModel(models.Model):
    CHOICE_GENDER=[
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    ]   
    CHOICE_BLOOD=[
        ('A-positive (A+)','A-positive (A+)'),
        ('A-negative (A-)','A-negative (A-)'),
        ('B-positive (B+)','B-positive (B+)'),
        ('B-negative (B-)','B-negative (B-)'),
        ('AB-positive (AB+)','AB-positive (AB+)'),
        ('AB-negative (AB-)','AB-negative (AB-)'),
        ('O-positive (O+)','O-positive (O+)'),
        ('O-negative (O-)','O-negative (O-)'),
    ]
    emp_name=models.ForeignKey(EmployeeModel,on_delete=models.CASCADE)
    emp_fullname=models.CharField(max_length=75)
    gender=models.CharField(max_length=20,choices=CHOICE_GENDER)
    blood_group=models.CharField(max_length=20,choices=CHOICE_BLOOD)
    dob=models.DateField()
    designation=models.CharField(max_length=50)
    contact_number=models.PositiveIntegerField()
    photo=models.ImageField(upload_to='media/',null=True,blank=True)
  
    def __str__(self):
        return f"{self.emp_fullname} : {self.designation}"

