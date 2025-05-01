from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('register/', views.register, name='register'),
    path('success/', views.registration_success, name='registration_success'),
]
