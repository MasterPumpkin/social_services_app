from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Import the decorator
from rest_framework import viewsets


# def index(request):
#     return redirect('admin:index')  # Redirect to the admin page

@login_required  # Apply the decorator to all relevant views
def clients(request):
    return render(request, 'frontend/clients.html')

@login_required
def add_client(request):
    return render(request, 'frontend/add_client.html')

@login_required
def employees(request):
    return render(request, 'frontend/employees.html')

@login_required
def add_employee(request):
    return render(request, 'frontend/add_employee.html')

@login_required
def visits(request):
    return render(request, 'frontend/visits.html')

@login_required
def add_visit(request):
    return render(request, 'frontend/add_visit.html')


#No login view needed