from django.urls import path

from . import views

urlpatterns = [
    path('', views.WorksAPIView.as_view(), name='works'),
    path('<int:work_id>/', views.WorksDetailAPIView.as_view(), name='work'),

    path('customers/', views.CustomersAPIView.as_view(), name='customers'),
    path('customers/<int:customer_id>/', views.CustomersDetailAPIView.as_view(), name='customers-detail'),

    path('employees/', views.EmployeesAPIView.as_view(), name='employees'),
    path('employees/<int:employee_id>/', views.EmployeesDetailAPIView.as_view(), name='employees-detail'),
]
