from django.urls import path

from . import views

urlpatterns = [
    path('', views.WorksAPIView.as_view(), name='works'),
    path('<int:work_id>/', views.WorksDetailAPIView.as_view(), name='work'),
    path('scratchpads/', views.ScratchpadAPIView.as_view(), name='scratchpad'),
    path('scratchpads/<int:scratchpad_id>/', views.ScratchpadDetailAPIView.as_view(), name='scratchpad-detail'),
    path(
        'scratchpads/<int:scratchpad_id>/records/<int:record_id>/',
        views.ScratchpadDetailRecordsAPIView.as_view(),
        name='scratchpad-record-detail'
    ),
]
