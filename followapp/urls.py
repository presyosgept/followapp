"""followapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from rest_framework.authtoken import views

from counselling.views import(
    SendFormEmail,
    # studentRefer_detail_view,
    SendFormEmail,
    student_list_view,
    # about_view,
   
 
    # export_studentslist,
    upload_studentslist,
    students_view,
    registerPage,
    loginPage,
    logoutUser,
    student_view,
    firstPage,
    verification_code,
    home,

    #admin
    admin_home_view,
    upload_faculty,
    upload_facultyload,
    upload_students,
    upload_studentsload,
  

    # teacher
    teacher_home_view,
    new,
    teacher_view_students,
    teacher_view_referred_students,
    teacher_coursecard,
    teacher_view_detail_referred_students,

    #counselor
    counselor_home_view,
    counselor_view_schedule,
    counselor_setSchedule,
    counselor_view_referred_students,
    notifications,
    # manual_detail,
    counselor_view_detail_referred_students,
    

    #director
    director_home_view,
    director_assign_counselor,
    director_fillinForm,
    # sample,

    #student
    student_home_view,
    student_schedule,
    notifications_student,
    student_notif_detail,

    # studentsList,
    CounselorList,
    SignUpFirstApi,
    VerificationApi,
    # RegisterApi,
    account,
    login_api,

    #uploaddb
    uploaddb_home_view,
    uploaddb_schooloffices,
    uploaddb_department,
    uploaddb_degreeprogram,
    uploaddb_allfaculty,
    uploaddb_allsubjects,
    uploaddb_semester,
    uploaddb_newoffercode,
    uploaddb_offercode
)


urlpatterns = [


    #uploaddb
    path('uploaddb/', uploaddb_home_view, name="uploaddb_home_view"),
    path('uploaddb/schooloffices', uploaddb_schooloffices, name="uploaddb_schooloffices"),
    path('uploaddb/department', uploaddb_department, name="uploaddb_department"),
    path('uploaddb/degreeprogram', uploaddb_degreeprogram, name="uploaddb_degreeprogram"),
    path('uploaddb/allfaculty', uploaddb_allfaculty, name="uploaddb_allfaculty"),
    path('uploaddb/allsubjects', uploaddb_allsubjects, name="uploaddb_allsubjects"),
    path('uploaddb/semester', uploaddb_semester, name="uploaddb_semester"),
    path('uploaddb/newoffercode', uploaddb_newoffercode, name="uploaddb_newoffercode"),
    path('uploaddb/offercode', uploaddb_offercode, name="uploaddb_offercode"),



    # path('student_api/', studentsList.as_view()),
    path('counselor_api/', CounselorList.as_view()),
    path('singupfirst_api/<str:id>/<str:email>', SignUpFirstApi.as_view()),
    path('verification_api/<str:id>/<str:code>', VerificationApi.as_view()),
    # path('register_api/<str:id>/<str:password>', RegisterApi.as_view()),
    path('email/', TemplateView.as_view(template_name="sendEmail.html"), name='sendEmail'),
    path('send-form-email',SendFormEmail.as_view(),name='send_email'),
    path('register', account),
    path('login_api', login_api),
    # path('account/register', create_auth),

    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),





    # path('firstpage/', firstPage, name='firstpage'),
    
    path('login/', loginPage, name='login'),
    path('', home, name='home'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerPage, name='register'),
    path('firstpage/', firstPage, name='firstpage'),
    path('verification_code/',verification_code, name ="verification_code"),
    

    #admin
    path('head/', admin_home_view, name="admin_home_view"),
    path('admin/upload_faculty', upload_faculty, name="upload_faculty"),
    path('admin/upload_facultyload', upload_facultyload, name="upload_facultyload"),
    path('admin/upload_students', upload_students, name="upload_students"),
    path('admin/upload_studentsload', upload_studentsload, name="upload_studentsload"),
 
    
    #teacher
    path('teacher/', teacher_home_view, name="teacher_home_view"),
    # path('teacher/referstudent',  refer_student, name="refer_student"),
    path('teacher/teacher_view_student/?P:<int:id>', teacher_view_students, name="teacher_view_students"),
    path('teacher/list_referred_students', teacher_view_referred_students, name="teacher_view_referred_students"),
    path('studentslist/new/?P:<int:stud>', new, name='new'), 
    path('teacher/teacher_coursecard', teacher_coursecard, name='teacher_coursecard'),
    path('studentslist/view_detail/?P:<int:id>', teacher_view_detail_referred_students, name='teacher_view_detail_referred_students'), 


    #counselor 
    path('counselor/', counselor_home_view, name="counselor_home_view"),
    path('counselor/schedule', counselor_view_schedule, name="counselor_view_schedule"),
    path('counselor/form/<str:pk>', counselor_setSchedule, name="counselor_setSchedule"),
    path('counselor/referredstudents', counselor_view_referred_students, name="counselor_view_referred_students"),
    path('counselor/notifications', notifications, name="notifications"),
    # path('counselor/manual_detail/<str:pk>/<str:created_by>/?P:<int:id>', manual_detail, name="manual_detail"),
    path('counselor/view_detail/?P:<int:id>', counselor_view_detail_referred_students, name='counselor_view_detail_referred_students'), 

   

    #student
    path('student/', student_home_view, name="student_home_view"),
    path('student/schedule', student_schedule, name="student_schedule"),
    path('student/notifications_student', notifications_student, name="notifications_student"),
    path('student/student_notif_detail/<str:pk>', student_notif_detail, name="student_notif_detail"),


    #director
    path('director/', director_home_view, name="director_home_view"),
    path('director/assign_counselor', director_assign_counselor, name="director_assign_counselor"),
    path('director/form/<str:pk>', director_fillinForm, name="director_fillinForm"),


    path('studentslist/studenthome', student_view, name="home_student"),
    path('studentslist/students', students_view),
    # path('studentslist/exportion', export_studentslist),
    # path('studentslist/upload_students', simple_upload_students),
    path('studentslist/upload', upload_studentslist),
    
   
    path('studentslist/', student_list_view, name='index'),
    # path('studentslist/about', about_view, name='about'),
    # path('students/<int:pk>/', studentRefer_detail_view),
    # path('products/<int:pk>/', product_detail_view),
    path('admin/', admin.site.urls),
]
