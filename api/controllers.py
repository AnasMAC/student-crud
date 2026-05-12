from django.http import JsonResponse
from .models import Student
import json


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

    student = Student.objects.get(student_id=id) 

    student.name = body.get('name', student.name)
    student.email = body.get('email', student.email)
    student.birth_year = body.get('birth_year', student.birth_year)
    student.enrollment_year = body.get('enrollment_year', student.enrollment_year)

    student.save()

    return JsonResponse({
        "message": "Student updated"
    })



def deleteStudent(request, id):
    student = Student.objects.get(student_id=id) 

    student.delete()

    return JsonResponse({
        "message": "Student deleted"
    })


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
    




