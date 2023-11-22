from django.urls import path

from . import views

urlpatterns = [
    path('employees/', views.EmployeesAPIView.as_view(), name='employees'),
    path('customers/', views.CustomersAPIView.as_view(), name='customers'),
]
