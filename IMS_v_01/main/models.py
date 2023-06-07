from django.db import models


# Create your models here.
class Student(models.Model):
    std_ID = models.BigAutoField(primary_key=True)
    std_fname = models.CharField(max_length=30)
    std_lname = models.CharField(max_length=30)
    std_bod = models.DateField()
    std_email = models.EmailField()
    std_pnum = models.IntegerField()
    std_nic = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.std_ID} - {self.std_fname} {self.std_lname}'


class Teacher(models.Model):
    t_ID = models.BigAutoField(primary_key=True)
    t_fname = models.CharField(max_length=30)
    t_lname = models.CharField(max_length=30)
    t_bod = models.DateField()
    t_email = models.EmailField()
    t_pnum = models.IntegerField()
    t_nic = models.CharField(max_length=12)


class Course(models.Model):
    course_ID = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    course_description = models.TextField()
    course_fee = models.DecimalField(max_digits=10, decimal_places=2)
    teacher_ID = models.ManyToManyField(Teacher, through='TeacherEnroll')
    student = models.ManyToManyField(Student, through='StudentEnroll')


class TeacherEnroll(models.Model):
    t_ID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)


class StudentEnroll(models.Model):
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)
    std_ID = models.ForeignKey(Student, on_delete=models.CASCADE)


class Attendance(models.Model):
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)
    std_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    att_date = models.DateTimeField()


class Payment(models.Model):
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)
    std_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment_ID = models.BigAutoField(primary_key=True)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Salary(models.Model):
    t_ID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    salary_ID = models.BigAutoField(primary_key=True)
    salary_amount = models.DecimalField(max_digits=12, decimal_places=2)
    salary_date = models.DateField()