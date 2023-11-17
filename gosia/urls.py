from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('employees/', include('employees.urls')),
    path('works/', include('works.urls')),
]
