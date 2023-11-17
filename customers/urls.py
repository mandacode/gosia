from django.urls import path

from . import views

urlpatterns = [
    path('', views.CustomersAPIView.as_view(), name='customers'),
    path('<int:customer_id>/', views.CustomersDetailAPIView.as_view(), name='customers-detail'),
]
