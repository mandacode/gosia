from django.contrib import admin
from django.urls import path, include

from works import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('works/', include('works.urls', namespace='works')),
    path('scratchpads/', include('scratchpads.urls', namespace='scratchpads')),
    path('invoices/', include('invoices.urls', namespace='invoices')),
    path('users/', include('users.urls')),

    path('accounts/', include("django.contrib.auth.urls")),
    path('', views.dashboard_view, name='dashboard')
]
