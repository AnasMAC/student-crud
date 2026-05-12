from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=257)
    enrollment_year = models.DateTimeField("Enrollement year")
    birth_year = models.DateTimeField("Birth year")

    def __str__(self):
        return f"{self.student_id}: \t\t{self.name}\n\t\t{self.email}\n\t\t{self.enrollment_year}\n\t\t{self.birth_year}"