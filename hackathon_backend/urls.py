from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView  # Asosiy sahifa uchun

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # API uchun
    path('', TemplateView.as_view(template_name='index.html')),  # Asosiy sahifa
]
