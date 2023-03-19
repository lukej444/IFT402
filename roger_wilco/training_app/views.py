from django.shortcuts import render

# These definitions connect the html pages to their URLs (WD 3/19/23).
def login(request):
	context = {}
	return render(request, 'training_app/login.html', context)

def current_training(request):
	return render(request, "training_app/current_training.html")

def training_search(request):
	return render(request, "training_app/training_search_tool.html")

def emp_search(request):
	return render(request, "training_app/employee_search.html")

def add_emp(request):
	return render(request, "training_app/add_employee.html")

def net_stat(request):
	return render(request, "training_app/network_status.html")

def sys_stat(request):
	return render(request, "training_app/sys_status.html")

def db_stat(request):
	return render(request, "training_app/database_status.html")

