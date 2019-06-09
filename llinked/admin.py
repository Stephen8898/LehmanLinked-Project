from django.contrib import admin
from .models import Department, Student, Instructor, Alumni, Course

# Register your models here.
# admin.site.register(Lehmanuser)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Alumni)
admin.site.register(Course)
