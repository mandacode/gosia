from django.urls import path

from . import views

urlpatterns = [
    path('', views.EmployeesAPIView.as_view(), name='employees'),
    path('<int:employee_id>/', views.EmployeesDetailAPIView.as_view(), name='employees-detail'),
]
