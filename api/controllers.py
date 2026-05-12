from django.http import JsonResponse
from .models import Student


class StudentController():
    @staticmethod
    def getStudents():
        students = Student.objects.all()

        data = []
        for student in students:
            data.append({
                "id": student.id,
                "title": student.title,
                "author": student.author,
                "published_year": student.published_year
            })

        return JsonResponse(data, safe=False)