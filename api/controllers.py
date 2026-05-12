import json

from django.http import JsonResponse
from .models import Student


def getStudents(request):
    students = Student.objects.all()

    data = []
    for student in students:
        data.append({
            "id": student.student_id,
            "name": student.name,
            "email": student.email,
            "enrollment_year": student.enrollment_year,
            "birth_year": student.birth_year
        })

    return JsonResponse(data, safe=False)

def modifyStudent(request, id):
    body = json.loads(request.body)

    student = Student.objects.get(id=id) 

    student.name = body.get('name', student.name)
    student.email = body.get('email', student.email)
    student.birth_year = body.get('birth_year', student.birth_year)
    student.enrollment_year = body.get('enrollment_year', student.enrollment_year)

    student.save()

    return JsonResponse({
        "message": "Book updated"
    })



def deleteStudent(request, id):
    student = Student.objects.get(id=id) 

    student.delete()

    return JsonResponse({
        "message": "Book deleted"
    })
