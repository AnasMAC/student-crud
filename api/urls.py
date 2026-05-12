from django.urls import path
from .views import student_router

urlpatterns = [
    path('students/', student_router),
]