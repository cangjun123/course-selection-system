from django.shortcuts import render, redirect
from .models import Course, Student

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def student_detail(request, student_id):
    student = Student.objects.get(student_id=student_id)
    courses = Course.objects.filter()
    return render(request, 'student_detail.html', {'student': student, 'all_courses':courses})

def add_course(request, student_id, course_id):
    student = Student.objects.get(student_id=student_id)
    course = Course.objects.get(pk=course_id)
    student.courses.add(course)
    return redirect('student_detail', student_id=student_id)

def drop_course(request, student_id, course_id):
    student = Student.objects.get(student_id=student_id)
    course = Course.objects.get(pk=course_id)
    student.courses.remove(course)
    return redirect('student_detail', student_id=student_id)