from django.urls import path

from . import views

urlpatterns = [
    path('', views.ScratchpadAPIView.as_view(), name='scratchpad'),
    path('<int:scratchpad_id>/', views.ScratchpadDetailAPIView.as_view(), name='scratchpad-detail'),
    path(
        '<int:scratchpad_id>/records/<int:record_id>/',
        views.ScratchpadDetailRecordsAPIView.as_view(),
        name='scratchpad-record-detail'
    )
]
