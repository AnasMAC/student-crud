from django.http import JsonResponse
from .models import Student
import json


def getStudents():
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

def postStudents(request):
    data=json.loads(request.body)
    new_student = Student.objects.create(
                name=data.get("name"),
                email=data.get("email"),
                password=data.get("password"),
                enrollment_year=data.get("enrollment_year"),
                birth_year=data.get("birth_year")
            )
    return JsonResponse({
                "message": "Student created successfully!",
                "id": new_student.student_id
            }, status=201)
    




