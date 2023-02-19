from email.policy import default
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Employee(models.Model):
	Employee_ID = models.IntegerField(primary_key=True)
	Last_Name = models.CharField(max_length=16)
	First_Name = models.CharField(max_length=16)
	Street_Address = models.CharField(max_length=75)
	City = models.CharField(max_length=16)
	State = models.CharField(max_length=10)
	Zip_Code = models.IntegerField(default=00000)
	Job_Assignment = models.CharField(max_length=25)
	Department_ID = models.ForeignKey(Department, on_delete=models.CASCADE)
	Supervisor_ID = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
	

	def __str__(self):
		return self.Employee_ID

class Department(models.Model):
	Department_ID = models.IntegerField(primary_key=True)
	Department_Name = models.CharField(max_length=50)
	Supervisor_ID = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

	def __str__(self):
		return self.Department_ID

class Supervisor(models.Model):
	Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
	Department_ID = models.ForeignKey(Department, on_delete=models.CASCADE)

	def __str__(self):
		return self.Employee_ID

class Training(models.Model):
	Training_ID = models.IntegerField()

	Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
