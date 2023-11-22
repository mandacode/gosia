from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('works/', include('works.urls')),
    path('scratchpads/', include('scratchpads.urls')),
    path('users/', include('users.urls')),
]
