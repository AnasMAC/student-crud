from django.shortcuts import render
import controllers as StudentController
from django.http import JsonResponse

# Create your views here.
def student_router(request):
    if request.method == 'GET':
        return StudentController.getStudents(request)
    elif request.method == 'POST':
        pass
    data = {
        'message': 'Route not found'
    }
    return JsonResponse(data, status=404)

def id_student_router(request, id):
    if request.method == 'PATCH':
        return StudentController.modifyStudent(request, id)
    elif request.method == 'DELETE':
        return StudentController.deleteStudent(request, id)
    data = {
        'message': 'Route not found'
    }
    return JsonResponse(data, status=404)