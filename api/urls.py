from django.urls import path
from .views import student_router, id_student_router

urlpatterns = [
    path('students', student_router),
    path('students/<int:id>', id_student_router),
]