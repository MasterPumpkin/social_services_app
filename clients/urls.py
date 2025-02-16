from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet) # zaregistruje /api/clients/ a /api/clients/<id>/

urlpatterns = [
    path('', include(router.urls)),
]