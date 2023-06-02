from django.contrib import admin
from .models import Student, Teacher, Course, TeacherEnroll, StudentEnroll, Payment, Attendance, Salary


# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(TeacherEnroll)
admin.site.register(StudentEnroll)
admin.site.register(Payment)
admin.site.register(Attendance)
admin.site.register(Salary)
