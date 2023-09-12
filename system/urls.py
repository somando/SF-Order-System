from django.urls import path
from . import views

app_name = 'system'

urlpatterns = [
    path('backyard/', views.backyard, name='backyard'),
    path('csrf_token/', views.csrf_token, name="csrf_token"),
]
