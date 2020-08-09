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


def staff_home(request):
    return render(request, "staff_template/main_content.html")

def add_files(request):
    return render(request,"staff_template/add_files.html")

def staff_agenda(request):
    return render(request, "staff_template/add_agenda.html")

def add_agenda_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        classes = request.POST.get("classes")
        skills = request.POST.get("skills")
        subtopic = request.POST.get("subtopic")
        agenda = request.FILES['agenda']
        fs = FileSystemStorage()
        filename = fs.save(agenda .name, agenda )
        profile_pic_url = fs.url(filename)

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=2)
            user.staffs.classes = classes
            user.staffs.skills = skills
            user.staffs.subtopic = subtopic
            user.staffs.agenda = agenda
            user.save()
            messages.success(request, "Successfully Uploaded the URL OR PDF")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request, "Failed to Upload the URL OR PDF")
            return HttpResponseRedirect(reverse("staff_files"))


def add_files_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        classes = request.POST.get("classes")
        skills = request.POST.get("skills")
        url = request.POST.get("url")
        pdffs = request.FILES['pdffs']
        fs = FileSystemStorage()
        filename = fs.save(pdffs .name, pdffs )
        profile_pic_url = fs.url(filename)

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=2)
            user.staffs.classes = classes
            user.staffs.skills = skills
            user.staffs.url = url
            user.staffs.pdf = pdf
            user.save()
            messages.success(request, "Successfully Uploaded the Agenda")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request, "Failed to Upload the Agenda")
            return HttpResponseRedirect(reverse("staff_agenda"))

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
