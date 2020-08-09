import json

# import requests
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from skill_app.models import Courses ,Students,Links,CustomUser
from twilio.rest import Client



def staff_home(request):
    # course = request.POST.get("course")
    # subjects = Subjects.objects.filter(course_id=course).filter(staff_id=request.user.id)
    return render(request, "staff_template/main_content.html")

def select_student_class(request):
    courses = Courses.objects.all()
    return render(request, "staff_template/select_student_class_template.html", {"courses": courses})

def manage_student(request):
    course = request.POST.get("course")
    students = Students.objects.filter(course_id=course)
    return render(request, "staff_template/manage_student_template.html", {"students": students})

def send_sms(request,student_id):
    user=Students.objects.get(id=student_id)
    x=str(user.ph_no)
    print(x,user)
    account_sid = 'ACb509d200fbfd37b8d26d99620a61e985'
    auth_token = 'b8be08d19afe7ea48dd81af445e2bc12'
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="https://google.com",
                     from_='+13344024332',
                     to='+91'+ x
                 )
    print(message.sid)
    return HttpResponseRedirect(reverse('manage_student'))

def send_whatsapp(request,student_id):
    user=Students.objects.get(id=student_id)
    x=str(user.ph_no)
    print(x,user)
    account_sid = 'ACb509d200fbfd37b8d26d99620a61e985'
    auth_token = 'b8be08d19afe7ea48dd81af445e2bc12'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="https://google.com",
                        from_='whatsapp:+14155238886',
                        to='whatsapp:+91'+x
                    )
    print(message.sid)
    return HttpResponseRedirect(reverse('manage_student'))


def add_link(request):
    return render(request, "staff_template/add_link.html")


def add_link_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        link = request.POST.get("link")
        # try:
        print(request.user.id)
        course_model = Links(url=link,staff_id_id=request.user)
        print(course_model.staff_id_id)
        # course_model1=CustomUser(id=request.user.id)
        course_model.save()
        # course_model1.save()
        messages.success(request, "Successfully Added Link")
        return HttpResponseRedirect(reverse("add_link"))
        # except:
        #     messages.error(request, "Failed to Add Link")
        #     return HttpResponseRedirect(reverse("add_link"))



