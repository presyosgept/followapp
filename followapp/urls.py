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
    loginPage,
    signup,
    logoutUser,
    register,
    verification_code,
    home,

    #admin
    admin_home_view,
    upload_faculty,
    upload_facultyload,
    upload_students,
    upload_studentsload,
    admin_offering,
    admin_view_offering,
    admin_department_choice,
  

    # teacher
    teacher_home_view,
    new,
    teacher_view_students,
    teacher_view_referred_students,
    teacher_coursecard,
    teacher_view_detail_referred_students,
    teacher_view_notif_detail,
    notifications_teacher,
    counselor_view_another_sched,

    #counselor
    counselor_home_view,
    counselor_view_schedule,
    counselor_setSchedule,
    counselor_view_referred_students,
    counselor_detail_schedule_counseling,
    counselor_detail_schedule_class,
    counselor_feedback,
    notifications,
    # manual_detail,
    counselor_view_detail_referred_students,
    counselor_view_pending_students,
    counselor_view_appointment,
    counselor_view_feedback,
    counselor_view_detail_feedback,
    

    #director
    director_home_view,
    director_assign_counselor,
    director_fillinForm,

    #student
    student_home_view,
    student_schedule,
    notifications_student,
    student_notif_detail,
    view_schedule_student,
    view_class_students,
    view_appointment_students,

    #api
    CounselorList,
    RegisterApi,
    VerificationApi,
    signup_api,
    login_api,

    #uploaddb
    uploaddb_home_view,
    uploaddb_schooloffices,
    uploaddb_department,
    uploaddb_degreeprogram,
    uploaddb_allfaculty,
    uploaddb_allsubject,
    uploaddb_semester,
    uploaddb_offercode,
    uploaddb_counselor,
)


urlpatterns = [


    #uploaddb
    path('uploaddb/', uploaddb_home_view, name="uploaddb_home_view"),
    path('uploaddb/schooloffices', uploaddb_schooloffices, name="uploaddb_schooloffices"),
    path('uploaddb/department', uploaddb_department, name="uploaddb_department"),
    path('uploaddb/degreeprogram', uploaddb_degreeprogram, name="uploaddb_degreeprogram"),
    path('uploaddb/allfaculty', uploaddb_allfaculty, name="uploaddb_allfaculty"),
    path('uploaddb/allsubjects', uploaddb_allsubject, name="uploaddb_allsubjects"),
    path('uploaddb/semester', uploaddb_semester, name="uploaddb_semester"),
    path('uploaddb/offercode', uploaddb_offercode, name="uploaddb_offercode"),
    path('uploaddb/counselor', uploaddb_counselor, name="uploaddb_counselor"),



    # path('student_api/', studentsList.as_view()),
    path('counselor_api/', CounselorList.as_view()),
    path('register_api/<str:id>/<str:email>', RegisterApi.as_view()),
    path('verification_api/<str:id>/<str:code>', VerificationApi.as_view()),
    # path('register_api/<str:id>/<str:password>', RegisterApi.as_view()),
    path('signup_api', signup_api),
    path('login_api', login_api),
    # path('account/register', create_auth),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),




    
    path('', home, name='home'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('signup/', signup, name='signup'),
    path('register/', register, name='register'),
    path('verification_code/',verification_code, name ="verification_code"),
    

    #admin
    path('head/', admin_home_view, name="admin_home_view"),
    path('admin/upload_faculty', upload_faculty, name="upload_faculty"),
    path('admin/upload_facultyload', upload_facultyload, name="upload_facultyload"),
    path('admin/upload_students', upload_students, name="upload_students"),
    path('admin/upload_studentsload', upload_studentsload, name="upload_studentsload"),
    path('admin/admin_offering', admin_offering, name="admin_offering"),
    path('admin/admin_view_offering', admin_view_offering, name="admin_view_offering"),
    path('admin/admin_department_choice', admin_department_choice, name="admin_department_choice"),
    
    
    
    #teacher
    path('teacher/', teacher_home_view, name="teacher_home_view"),
    # path('teacher/referstudent',  refer_student, name="refer_student"),
    path('teacher/teacher_view_student/?P:<int:id>', teacher_view_students, name="teacher_view_students"),
    path('teacher/list_referred_students', teacher_view_referred_students, name="teacher_view_referred_students"),
    path('studentslist/new/?P:<int:stud>/?P:<int:id>', new, name='new'), 
    path('teacher/teacher_coursecard', teacher_coursecard, name='teacher_coursecard'),
    path('teacher/view_detail/?P:<int:id>', teacher_view_detail_referred_students, name='teacher_view_detail_referred_students'), 
    path('teacher/teacher_view_notif_detail/?P:<int:id>', teacher_view_notif_detail, name='teacher_view_notif_detail'), 
    path('teacher/notifications', notifications_teacher, name="notifications_teacher"),
    path('teacher/counselor_view_another_sched/?P:<int:num>', counselor_view_another_sched, name='counselor_view_another_sched'), 
    


    #counselor 
    path('counselor/', counselor_home_view, name="counselor_home_view"),
    path('counselor/schedule', counselor_view_schedule, name="counselor_view_schedule"),
    path('counselor/form/<str:pk>', counselor_setSchedule, name="counselor_setSchedule"),
    path('counselor/referredstudents', counselor_view_referred_students, name="counselor_view_referred_students"),
    path('counselor/notifications', notifications, name="notifications"),
    # path('counselor/manual_detail/<str:pk>/<str:created_by>/?P:<int:id>', manual_detail, name="manual_detail"),
    path('counselor/view_detail/?P:<int:id>', counselor_view_detail_referred_students, name='counselor_view_detail_referred_students'), 
    path('counselor/counselor_detail_schedule_counseling/<str:start>/<str:end>/<str:date>', counselor_detail_schedule_counseling, name="counselor_detail_schedule_counseling"),
    path('counselor/counselor_detail_schedule_class/<str:offer_code>/<str:sem_id>/<str:year>', counselor_detail_schedule_class, name="counselor_detail_schedule_class"),
    path('counselor/counselor_feedback/?P:<int:id>', counselor_feedback, name='counselor_feedback'), 
    path('counselor/pendingstudents', counselor_view_pending_students, name="counselor_view_pending_students"),
    path('counselor/counselor_view_appointment/?P:<int:id>', counselor_view_appointment, name='counselor_view_appointment'), 
    path('counselor/counselor_view_feedback', counselor_view_feedback, name="counselor_view_feedback"),
    path('counselor/counselor_view_detail_feedback/?P:<int:id>', counselor_view_detail_feedback, name='counselor_view_detail_feedback'), 
    


    #student
    path('student/', student_home_view, name="student_home_view"),
    path('student/schedule', student_schedule, name="student_schedule"),
    path('student/view_schedule_student', view_schedule_student, name="view_schedule_student"),
    path('student/notifications_student', notifications_student, name="notifications_student"),
    path('student/student_notif_detail/?P:<int:id>', student_notif_detail, name="student_notif_detail"),
    path('student/view_class_students/<str:offer_code>/<str:sem_id>/<str:year>', view_class_students, name="view_class_students"),
    path('student/view_appointment_students/<str:start>/<str:end>/<str:date>', view_appointment_students, name="view_appointment_students"),




    #director
    path('director/', director_home_view, name="director_home_view"),
    path('director/assign_counselor', director_assign_counselor, name="director_assign_counselor"),
    path('director/form/<str:pk>', director_fillinForm, name="director_fillinForm"),


    path('admin/', admin.site.urls),
]
