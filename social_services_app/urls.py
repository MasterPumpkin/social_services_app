from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clients.urls')),  # Add URL patterns for clients app
    path('api/', include('employees.urls')),
    path('api/', include('visits.urls')),
    path('api/', include('attendance.urls')),
]
