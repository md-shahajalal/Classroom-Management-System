from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from .models import Notice, ClassRoom, Faculty, Course, Class
# Create your views here.


def index(request):
    if(request.method == 'POST'):

       
        # for ClassRoom   
        if 'addClassRoomForm' in request.POST.keys():
            classroom_used_for = request.POST.get('inlineRadioOptions', '')
            classroom_no = request.POST.get('classroomnumber','')
            if(classroom_no !=''):
                classroom = ClassRoom(
                    classroom_used_for=classroom_used_for, classroom_no=classroom_no)
                classroom.save()
        

        # for Course
        if 'addCourseForm' in request.POST.keys():
            course_semester = request.POST.get('semester', '')
            course_type = request.POST.get('courseTypeOptions', '')
            course_code = request.POST.get('courseCode', '')
            course_name = request.POST.get('courseTitle', '')
            if(course_code != ''):
                course = Course(course_semester=course_semester, course_type=course_type,
                                course_code=course_code, course_name=course_name)
                course.save()
    #teachers
    assigned_teachers=Faculty.objects.all()
    #classroom
    classrooms=ClassRoom.objects.all()
    courses=Course.objects.all()

    params={'assigned_teachers':assigned_teachers,'classrooms':classrooms,'courses':courses}
    return render(request, 'admintemp/homepage.html',params)

#insert cllass
def insert(request):
    class_semester=request.POST['semester']
    class_course_code=request.POST['courseCode']
    class_course_name=request.POST['courseName']
    class_assigned_teacher=request.POST['teacher']
    class_date=request.POST['classDate']
    class_time=request.POST['classTime']
    class_duration=request.POST['duration']
    class_classroom=request.POST['classRoom']
    
    class1 = Class(class_semester=class_semester,class_course_code=class_course_code,
    class_course_name=class_course_name,class_assigned_teacher=class_assigned_teacher,
    class_date=class_date,class_time=class_time,class_duration=class_duration,
    class_classroom=class_classroom)

    class1.save()
    return redirect('/')

#insert notice to database
def insertnotice(request):
    notice_title=request.POST['notice_title']
    notice_description=request.POST['notice_description']

    notice=Notice(notice_title=notice_title,notice_description=notice_description)
    notice.save()
    return redirect('/')

#insert faculty
def insertfaculty(request):
    faculty_name=request.POST['faculty_name']
    faculty_designation=request.POST['faculty_designation']
    faculty=Faculty(faculty_name=faculty_name,faculty_designation=faculty_designation)
    faculty.save()
    return redirect('/')

