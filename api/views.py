from django.shortcuts import render
from . import controllers as StudentController
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_router(request):
    if request.method == 'GET':
        return StudentController.getStudents()
    elif request.method == 'POST':
        return StudentController.postStudents(request)
