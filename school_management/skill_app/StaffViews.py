from django.shortcuts import render
from django.urls import reverse
from .models import Courses ,Students
from twilio.rest import Client
from django.http import HttpResponseRedirect


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




