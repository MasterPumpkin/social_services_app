from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, clients, add_client, employees, add_employee, visits, add_visit

router = DefaultRouter()
# router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', home, name='home'),
    # path('', index, name='index'),  # Add this for the index page
    # path('login/', login, name='login'), # Add for login page
    path('clients/', clients, name='clients'),
    path('add_client/', add_client, name='add_client'),
    path('employees/', employees, name='employees'),
    path('add_employee/', add_employee, name='add_employee'),
    path('visits/', visits, name='visits'),
    path('add_visit/', add_visit, name='add_visit'),
    path('api/', include(router.urls)), # Keep API routes

]