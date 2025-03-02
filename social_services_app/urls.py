from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clients.urls')),
    path('api/', include('employees.urls')),
    path('api/', include('visits.urls')),
    path('api/', include('attendance.urls')),
    path('api/users/', include('users.urls')), # Změna: Přidáno users/
    path('', include('frontend.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), # Ponecháme pro Django administraci
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)