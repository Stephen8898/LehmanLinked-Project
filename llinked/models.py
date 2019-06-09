from django.db import models
from django.contrib.auth.models import User
# from .models import Post
from django.utils import timezone
# Create your models here.


class Alumni(models.Model):
    id = models.BigIntegerField(primary_key=True, default=0)
    user = models.OneToOneField(User,  on_delete=models.CASCADE, db_column='user', blank=True, null=True)
    grad_date = models.DateField()

    def __str__(self):
        return '%s, %s' %  (self.user, self.grad_date)

    class Meta:
        db_table = 'alumni'


class Course(models.Model):
    course_id = models.BigIntegerField(primary_key=True)
    course_name = models.CharField(max_length=60)
    dept = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept', blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.course_name, self.dept)

    class Meta:
        db_table = 'course'
        

class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    dept_name = models.CharField(max_length=60)

    def  __str__(self):
        return '%s' % (self.dept_name)

    class Meta:
        db_table = 'department'

class Instructor(models.Model):
    id = models.BigIntegerField(primary_key=True, default=0)
    user = models.OneToOneField(User,  on_delete=models.CASCADE, db_column='user', blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept', blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.user, self.dept)

    class Meta:
        db_table = 'instructor'



class Student(models.Model):
    id = models.BigIntegerField(primary_key=True, default=0)
    user = models.OneToOneField(User,  on_delete=models.CASCADE, db_column='user', blank=True, null=True)
    major = models.ForeignKey(Department, models.DO_NOTHING, db_column='major', related_name= 'major', blank=True, null=True)
    minor = models.ForeignKey(Department, models.DO_NOTHING, db_column='minor', related_name='minor', blank=True, null=True)
    courseid = models.ManyToManyField(Course, verbose_name='Student Courses')

    def __str__(self):
        return '%s, %s, %s' % (self.user, self.major, self.minor)

    class Meta:
        db_table = 'student'

# class Post(models.Model):
#     id = models.BigIntegerField(primary_key=True, default=0)
#     title = models.CharField(max_length=150, null=False, default='Bio')
#     content = models.TextField(max_length=600, null=False, default='Fill out yout bio')
#     # date_published = models.DateTimeField(default=timezone.now)
  

#     def __str__(self):
#         return '%s, %s' % (self.title, self.content)

#     class Meta:
#         db_table = 'post'