from . import controllers as StudentController
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def student_router(request):
    if request.method == 'GET':
        return StudentController.getStudents(request)
    elif request.method == 'POST':
        return StudentController.postStudents(request)

    data = {
        'message': 'Route not found'
    }
    return JsonResponse(data, status=404)
@csrf_exempt
def id_student_router(request, id):
    if request.method == 'PATCH':
        return StudentController.modifyStudent(request, id)
    elif request.method == 'DELETE':
        return StudentController.deleteStudent(request, id)
    data = {
        'message': 'Route not found'
    }
    return JsonResponse(data, status=404)