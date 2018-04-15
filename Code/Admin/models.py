from django.db import models


class Class(models.Model):
    class_name = models.CharField(max_length=100)
    class_strength = models.IntegerField
    class_teacher = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    cl = models.ForeignKey(Class, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)

class Results(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Language_1 = models.IntegerField
    Language_2 = models.IntegerField
    Maths = models.IntegerField
    Science = models.IntegerField
    Social = models.IntegerField
    Total = models.IntegerField
    Year = models.CharField(max_length=100)
    Exam_Type = models.IntegerField
    cl_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    Rank = models.IntegerField()

class TotalMarks(models.Model):
    T_Language_1 = models.IntegerField
    T_Language_2 = models.IntegerField
    T_Maths = models.IntegerField
    T_Science = models.IntegerField
    T_Social = models.IntegerField
    T_Total = models.IntegerField
    T_Year = models.CharField(max_length=100)
    T_Exam_Type = models.IntegerField
    T_cl_id = models.ForeignKey(Class, on_delete=models.CASCADE)

class Attendance(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Year = models.CharField(max_length=100)
    Class_Attended = models.IntegerField
    Total_Classes = models.IntegerField

class Login(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "Student : " + self.student_id.name
