from django.urls import path
from . import views

urlpatterns = [
    path('qr_code_display/', views.qr_generator, name = 'qr_code_display'),
    path('', views.qr_generator, name = 'qr_generator'),
]