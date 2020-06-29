from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/notes/', include('api.urls')),
    path('auth/', obtain_auth_token),
]
