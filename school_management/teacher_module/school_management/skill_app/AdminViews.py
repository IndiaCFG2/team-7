import json

# import requests
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from skill_app.models import CustomUser

from skill_app.models import Courses, Subjects, Staffs, Students


def admin_home(request):
    return render(request, "admin_template/main_content.html")


def add_staff(request):
    return render(request, "admin_template/add_staff_template.html")


def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        qualification = request.POST.get("qualification")
        dob = request.POST.get("dob")
        blood_group = request.POST.get("blood_group")
        teacher_roll_number = request.POST.get("teacher_roll_number")
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        ph_no = request.POST.get("ph_no")

        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=2)
            user.staffs.gender = gender
            user.staffs.address = address
            user.staffs.ph_no = ph_no
            user.staffs.dob = dob
            user.staffs.qualification = qualification
            user.staffs.blood_group = blood_group
            user.staffs.teacher_roll_number = teacher_roll_number
            user.staffs.profile_pic = profile_pic_url
            user.save()
            messages.success(request, "Successfully Added Staff")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request, "Failed to Add Staff")
            return HttpResponseRedirect(reverse("add_staff"))


def add_course(request):
    return render(request, "admin_template/add_course_template.html")


def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Successfully Added Course")
            return HttpResponseRedirect(reverse("add_course"))
        except:
            messages.error(request, "Failed to Add Course")
            return HttpResponseRedirect(reverse("add_course"))


def add_student(request):
    courses = Courses.objects.all()
    return render(request, "admin_template/add_student_template.html", {"courses": courses})


def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        first_name = request.POST.get("first_name")
        password = request.POST.get("password")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        parent_username = request.POST.get("parent_username")
        blood_group = request.POST.get("blood_group")
        email = request.POST.get("email")
        address = request.POST.get("address")
        roll_number = request.POST.get("roll_number")
        gender = request.POST.get("gender")
        ph_no = request.POST.get("ph_no")
        dob = request.POST.get("dob")
        course_id = request.POST.get("course")
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

        try:
            user = CustomUser.objects.create_user(username=username, password=password,
                                                  email=email, last_name=last_name, first_name=first_name, user_type=3)
            user.students.address = address
            course_obj = Courses.objects.get(id=course_id)
            user.students.course_id = course_obj
            user.students.gender = gender
            user.students.roll_number = roll_number
            user.students.dob = dob
            user.students.blood_group = blood_group
            user.students.ph_no = ph_no
            user.students.profile_pic = profile_pic_url

            user.save()
            messages.success(request, "Successfully Added Student Details")
            return HttpResponseRedirect(reverse("add_student"))
        except:
            messages.error(request, "Failed to Add Student Details")
            return HttpResponseRedirect(reverse("add_student"))


def add_subject(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request, "admin_template/add_subject_template.html", {"staffs": staffs, "courses": courses})


def add_subject_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        course = Courses.objects.get(id=course_id)
        staff_id = request.POST.get("staff")
        staff = CustomUser.objects.get(id=staff_id)
        try:
            subject = Subjects(subject_name=subject_name, course_id=course, staff_id=staff)
            subject.save()
            messages.success(request, "Successfully Added Skill")
            return HttpResponseRedirect(reverse("add_subject"))
        except:
            messages.error(request, "Failed to Add Skill")
            return HttpResponseRedirect(reverse("add_subject"))


@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_teacher_roll_number_exist(request):
    teacher_roll_number = request.POST.get("teacher_roll_number")
    user_obj = Staffs.objects.filter(teacher_roll_number=teacher_roll_number).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_roll_number_exist(request):
    roll_number = request.POST.get("roll_number")
    user_obj = Students.objects.filter(roll_number=roll_number).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
