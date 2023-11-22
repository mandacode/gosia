from django.urls import path

from . import views

urlpatterns = [
    path('', views.WorksAPIView.as_view(), name='works'),
    path('<int:work_id>/', views.WorksDetailAPIView.as_view(), name='work'),
]
