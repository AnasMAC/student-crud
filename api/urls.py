from django.urls import path
from .views import student_router

urlpatterns = [
    path('student/', student_router),
    path('student/<int:id>', ),
]