from django.db import models


class Class(models.Model):
    class_name = models.CharField(max_length=100)
    class_strength = models.IntegerField
    class_teacher = models.CharField(max_length=100)

    def __str__(self):
        return "Class : " + str(self.class_name)

class Student(models.Model):
    name = models.CharField(max_length=100)
    cl = models.ForeignKey(Class, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return "Student : " + str(self.name)

class TotalMarks(models.Model):
    T_Language_1 = models.IntegerField()
    T_Language_2 = models.IntegerField()
    T_Maths = models.IntegerField()
    T_Science = models.IntegerField()
    T_Social = models.IntegerField()
    T_Total = models.IntegerField()
    Year = models.CharField(max_length=100)
    Exam_Type = models.CharField(max_length=100)
    T_cl_id = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.T_cl_id) + "\t- " + str(self.Exam_Type) + "\t- " + str(self.Year)

class Results(models.Model):
    Exam_id = models.ForeignKey(TotalMarks, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Language_1 = models.IntegerField()
    Language_2 = models.IntegerField()
    Maths = models.IntegerField()
    Science = models.IntegerField()
    Social = models.IntegerField()
    Total = models.IntegerField()
    cl_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    Rank = models.IntegerField()

    def __str__(self):
        return "Student : " + str(self.student_id.name)


class Attendance(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Year = models.CharField(max_length=100)
    Class_Attended = models.IntegerField()
    month = models.CharField(max_length=100)
    Total_Classes = models.IntegerField()

    def __str__(self):
        return "Student : " + str(self.student_id.name)

class Login(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "Student : " + self.student_id.name
