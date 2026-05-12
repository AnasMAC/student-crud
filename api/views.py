from django.shortcuts import render
from .controllers import StudentController

# Create your views here.
def student_router(request):
    if request.method == 'GET':
        return StudentController.getStudents()
    elif request.method == 'POST':
        pass
