"""school_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from skill_app import views, AdminViews, StaffViews
from school_management import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo', views.showDemoPage),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.ShowLoginPage, name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user, name="logout"),
    path('doLogin', views.doLogin, name="do_login"),
    path('admin_home', AdminViews.admin_home, name="admin_home"),
    path('staff_home', StaffViews.staff_home, name="staff_home"),
    path('add_files_save', StaffViews.add_files_save, name="add_files_save"),
    path('add_agenda_save', StaffViews.add_agenda_save, name="add_agenda_save"),
    path('add_staff', AdminViews.add_staff, name="add_staff"),
    path('staff_agenda', StaffViews.staff_agenda, name="staff_agenda"),
    path('add_files', StaffViews.add_files, name="add_files"),
    path('add_staff_save', AdminViews.add_staff_save, name="add_staff_save"),
    path('add_course', AdminViews.add_course, name="add_course"),
    path('add_course_save', AdminViews.add_course_save, name="add_course_save"),
    path('add_student', AdminViews.add_student, name="add_student"),
    path('add_student_save', AdminViews.add_student_save, name="add_student_save"),
    path('add_subject', AdminViews.add_subject, name="add_subject"),
    path('add_subject_save', AdminViews.add_subject_save, name="add_subject_save"),
    path('check_email_exist', AdminViews.check_email_exist, name="check_email_exist"),
    path('check_teacher_roll_number_exist', AdminViews.check_teacher_roll_number_exist, name="check_teacher_roll_number_exist"),
    path('check_username_exist', AdminViews.check_username_exist, name="check_username_exist"),
    path('check_roll_number_exist', AdminViews.check_roll_number_exist, name="check_roll_number_exist"),
]
