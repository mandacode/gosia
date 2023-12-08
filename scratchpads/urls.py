from django.urls import path

from . import views

app_name = 'scratchpads'

urlpatterns = [
    path('', views.list_scratchpads_view, name='list'),
    path('create/', views.create_scratchpad_view, name='create'),
    path('<int:scratchpad_id>/', views.scratchpad_detail_view, name='detail'),
    path('<int:scratchpad_id>/generate_customer_invoice/', views.generate_customer_invoice_view, name='generate'),
]
