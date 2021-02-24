from django.db import models
from django.utils.timezone import now

# Create your models here.
class Notice(models.Model):
    #notice_id=models.AutoField(primary_key=True)
    notice_title=models.CharField(max_length=100,default="")
    notice_description=models.CharField(max_length=5000,default='nothing is posted')
    notice_timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.notice_title


    
    

class Faculty(models.Model):
    #faculty_id=models.AutoField(primary_key=True)
    faculty_name=models.CharField(max_length=50,default="")
    faculty_designation=models.CharField(max_length=30,default="")
    def __str__(self):
        return self.faculty_name
    

class Course(models.Model):
    #course_id=models.AutoField(primary_key=True)
    course_semester=models.CharField(max_length=50,default="")
    course_type=models.CharField(max_length=10,default='Theory')
    course_code=models.CharField(max_length=15,default="")
    course_name=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.course_name
     

class ClassRoom(models.Model):
    #classroom_id=models.AutoField(primary_key=True)
    classroom_no=models.CharField(max_length=10)
    classroom_used_for=models.CharField(max_length=10,default='Theory')
    def __str__(self):
        return self.classroom_no
     


class Class(models.Model):
    #class_id=models.AutoField(primary_key=True)
    class_semester=models.CharField(max_length=30,default="")
    class_course_code=models.CharField(max_length=10,default="")
    class_course_name=models.CharField(max_length=100,default="")
    class_assigned_teacher=models.CharField(max_length=50,default="")
    class_date=models.DateField()
    class_time=models.TimeField()
    class_duration=models.CharField(max_length=20,default="45 min")
    class_classroom=models.CharField(max_length=20,default="")

    class Meta:
        ordering =('class_semester',)
    def __str__(self):
        return self.class_course_code


