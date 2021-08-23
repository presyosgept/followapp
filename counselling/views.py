from typing import Counter
from django.db.models.fields import TimeField
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render, redirect 
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .utilities import create_notification
from django.views import generic
from django.utils import timezone
from datetime import date,datetime,timedelta

from .forms import StudentScheduleForm,CounselorScheduleForm,CounselorForm, TeachersReferralForm, StudentsForm,CreateUserForm, TeachersloadForm, SubjectOfferedForm, FacultyloadForm, StudentsloadForm
from .models import  Counselor,Notification,StudentSchedule,CounselorSchedule,Counselor,TeachersReferral, Students, Teachersload, SubjectOffered, Facultyload, Studentsload

from .resources import  StudentScheduleResource,CounselorScheduleResource,CounselorResource,TeachersReferralResource, StudentsResource,TeachersloadResource,SubjectOfferedResource,FacultyloadResource, StudentsloadResource
from tablib import Dataset

# Create your views here.

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import studentsSerializers,counselorSerializers

# Create your views here.

class studentsList(APIView):
    def get(self, request):
        stud = Students.objects.all()
        serializer=studentsSerializers(stud, many=True)
        return Response({'students':serializer.data})

class CounselorList(APIView):
    def get(self, request):
        couns = Counselor.objects.all()
        serializer=counselorSerializers(couns, many=True)
        return Response({'counselors':serializer.data})


















ihap = 0
ihap1 =0

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
                    flag = 0
                    username = request.POST.get('username')
                    qs = Students.objects.all()
                    for student in qs:
                        if student.studnumber ==username:
                            flag = 1
                    if flag == 1:
                        form = CreateUserForm(request.POST)
                        if form.is_valid():
                            form.save()
                            user = form.cleaned_data.get('username')
                            messages.success(request, 'Student Account was created for ' + user)
                        return redirect('login')
                    elif flag == 0:
                        qs = Teachersload.objects.all()
                        for teacher in qs:
                            if teacher.employeeid ==username:
                                form = CreateUserForm(request.POST)
                                if form.is_valid():
                                    form.save()
                                    user = form.cleaned_data.get('username')
                                    messages.success(request, ' Teacher/Counselor Account was created for ' + user)
                                return redirect('login')
                        
                    if username == 'followapp':
                        form = CreateUserForm(request.POST)
                        if form.is_valid():
                            form.save()
                            user = form.cleaned_data.get('username')
                            messages.success(request, ' Admin Account was created for ' + user)
                        return redirect('login')
                    elif username == 'director':
                        form = CreateUserForm(request.POST)
                        if form.is_valid():
                            form.save()
                            user = form.cleaned_data.get('username')
                            messages.success(request, ' Director Account was created for ' + user)
                        return redirect('login')
                    else:
                        messages.info(request, 'Check Credentials Account Not Created')  
    
	return render(request, 'register.html', {'form':form})


def loginPage(request):
	if request.user.is_authenticated:
            return redirect('home')    
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				if request.method == 'POST':
                                    flag = 0
                                    username = request.POST.get('username')
                                    qs = Students.objects.all()
                                    for student in qs:
                                        if student.studnumber ==username:
                                            if student.role == 'learner':
                                                flag = 1
                                    if flag == 1:
                                        request.session['username'] = username
                                        return redirect('student_home_view')
                                    else:
                                        qs = Teachersload.objects.all()
                                        for teacher in qs:
                                            if teacher.employeeid ==username:
                                                if teacher.role == 'teacher':
                                                        request.session['username'] = username
                                                        flag = 2
                                                elif teacher.role == 'counselor':
                                                        request.session['username'] = username
                                                        flag = 3
                                    if flag == 2:
                                            return redirect('teacher_home_view')
                                    if flag == 3:
                                            return redirect('counselor_home_view')
                                    if username == 'followapp':
                                        return redirect('admin_home_view')
                                    if username == 'director':
                                        return redirect('director_home_view')
			else:
				messages.info(request, 'Username OR password is incorrect')

		return render(request, 'login.html', {})


def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def firstpage(request, *args, **kwargs):
    return render(request, "firstpage.html", {})

#director
@login_required(login_url='login')
def director_home_view(request, *args, **kwargs):
    return render(request, "director/director_home.html", {})

@login_required(login_url='login')
def director_assign_counselor(request, *args, **kwargs):
    qs = Teachersload.objects.filter(role='counselor')
    context = {"object_list": qs}
    return render(request, "director/assign_counselor.html", context)

@login_required(login_url='login')
def director_fillinForm(request, pk):
    counselor = Counselor.objects.get(employeeid=pk)
    form = CounselorForm(instance=counselor)
    if request.method == "POST":
        print("chuchu")
        form = CounselorForm(request.POST, instance=counselor)
        if form.is_valid():
            form.save()
            return render(request, "director/director_home.html")
    context = {"form": form}
    return render(request, "director/form.html", context )

#director

#admin
@login_required(login_url='login')
def admin_home_view(request, *args, **kwargs):
    return render(request, "admin/admin_home.html", {})

@login_required(login_url='login')
def upload_counselor(request):
    if request.method == 'POST':
        CounselorResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
           
        	print(data[1])
        	value = Counselor(
                data[0],
                data[1], 
                data[2],   
                data[3], 
                )
        	value.save()     
    return render(request, "admin/upload_counselor.html")

@login_required(login_url='login')
def export_studentsload(request):
    Studentsload_resource = StudentsloadResource()
    dataset = Studentsload_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Studentsload.xls"'
    return response

@login_required(login_url='login')
def upload_studentsload(request):
    if request.method == 'POST':
        StudentsloadResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
           
        	print(data[1])
        	value = Studentsload(
                data[0],
                data[1], 
                data[2],   
                )
        	value.save()     
    return render(request, "admin/upload_studentsload.html")

@login_required(login_url='login')
def export_students(request):
    students_resource = StudentsResource()
    dataset = students_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="students.xls"'
    return response

@login_required(login_url='login')
def upload_students(request):
    if request.method == 'POST':
        StudentsResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
           
        	print(data[1])
        	value = Students(
                data[0],
                data[1], 
                data[2], 
                data[3],  
                data[4], 
                data[5], 
                data[6]
                )
        	value.save()     
    return render(request, "admin/upload_students.html")

@login_required(login_url='login')
def export_StudentSchedule(request):
    StudentSchedule_resource = StudentScheduleResource()
    dataset = StudentSchedule_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="StudentSchedule.xls"'
    return response

@login_required(login_url='login')
def upload_StudentSchedule(request):
    if request.method == 'POST':
        StudentScheduleResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
           
        	print(data[1])
        	value = StudentSchedule(
                data[0],
                data[1], 
                data[2], 
                data[3],  
                data[4],  
                )
        	value.save()     
    return render(request, "admin/upload_studentsched.html")

@login_required(login_url='login')
def export_CounselorSchedule(request):
    CounselorSchedule_resource = CounselorScheduleResource()
    dataset = CounselorSchedule_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="CounselorSchedule.xls"'
    return response

@login_required(login_url='login')
def upload_CounselorSchedule(request):
    if request.method == 'POST':
        CounselorScheduleResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
           
        	print(data[1])
        	value = CounselorSchedule(
                data[0],
                data[1], 
                data[2], 
                data[3],  
                data[4],  
                )
        	value.save()     
    return render(request, "admin/upload_counselorsched.html")

@login_required(login_url='login')
def export_teachersload(request):
    teachersload_resource = TeachersloadResource()
    dataset = teachersload_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="teachersload.xls"'
    return response

@login_required(login_url='login')
def upload_teachersload(request):
    if request.method == 'POST':
        TeachersloadResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
           
        	print(data[1])
        	value = Teachersload(
                data[0],
                data[1], 
                data[2], 
                data[3], 
                data[4], 
                )
        	value.save()     
    return render(request, "admin/upload_teachers.html")

@login_required(login_url='login')
def export_subject_offered(request):
    subject_offered_resource = SubjectOfferedResource()
    dataset = subject_offered_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="subject_offered.xls"'
    return response

@login_required(login_url='login')
def upload_subject_offered(request):
    if request.method == 'POST':
        SubjectOfferedResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
           
        	print(data[1])
        	value = SubjectOffered(
                data[0],
                data[1], 
                data[2], 
                data[3], 
                data[4], 
                data[5],
                data[6],
                )
        	value.save()     
    return render(request, "admin/upload_subject_offered.html")

@login_required(login_url='login')
def export_facultyload(request):
    facultyload_resource = FacultyloadResource()
    dataset = facultyload_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="facultyload.xls"'
    return response

@login_required(login_url='login')
def upload_facultyload(request):
    if request.method == 'POST':
        FacultyloadResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
           
        	print(data[1])
        	value = Facultyload(
                data[0],
                data[1],  
                )
        	value.save()     
    return render(request, "admin/upload_facultyload.html")

@login_required(login_url='login')
def export_studentsload(request):
    studentsload_resource = StudentsloadResource()
    dataset = studentsload_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="studentsload.xls"'
    return response

@login_required(login_url='login')
def upload_studentsload(request):
    if request.method == 'POST':
        StudentsloadResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
           
        	print(data[1])
        	value = Studentsload(
                data[0],
                data[1], 
                data[2],   
                )
        	value.save()     
    return render(request, "admin/upload_studentsload.html")


#admin

#teacher
@login_required(login_url='login')
def teacher_home_view(request, *args, **kwargs):
    user = request.session.get('username')
    qs = Facultyload.objects.filter(employeeid = user)
    context = {"object_list": qs}
    return render(request, "teacher/teacher_home.html", {"user": user} and context)

@login_required(login_url='login')
def new(request):
    user = request.session.get('username')
    name = ''
    stdnum= ''
    sub= ''
    couns =''
    global ihap
    global ihap1
    if request.method=="POST":
       firstname= request.POST['firstname']
       name = firstname
       lastname= request.POST['lastname']
       studnumber= request.POST['studnumber']
       stdnum= studnumber
       degree_program= request.POST['degree_program']
       subject_referred= request.POST['subject_referred']
       sub = subject_referred
       reasons= request.POST['reasons']
       qs = Counselor.objects.get(program_designation = degree_program)
       couns = qs.employeeid
       studentInfo = TeachersReferral(firstname=firstname, 
       lastname=lastname,studnumber=studnumber,
       degree_program = degree_program,subject_referred=subject_referred,
       reasons=reasons,counselor=qs.employeeid,employeeid=user)
       studentInfo.save()
       ihap = ihap + 1
       ihap1 = ihap1 + 1
       create_notification(couns, user, 'manual_referral', extra_id=int(stdnum))
    else:
        TeachersReferralForm()
    studentSched=StudentSchedule.objects.all()
    counselorSched= CounselorSchedule.objects.all()
    # for index, objectstud in enumerate(studentSched):
    #     if studentSched[index].schedule==None and studentSched[index+1].schedule==None:
    #         for index, object in enumerate(counselorSched):
    #             if counselorSched[index].service_offered==None and counselorSched[index+1].service_offered==None:
    #                 CounselorSchedule.objects.filter(schedid=counselorSched[index].schedid).update(
    #                     service_offered='COUNSELING',description=name)
    #                 CounselorSchedule.objects.filter(schedid=counselorSched[index+1].schedid).update(
    #                     service_offered='COUNSELING',description=name)
    #                 studentNumber= stdnum
    #                 subject= sub
    #                 teacher_referred= user
    #                 print(studentNumber,subject,teacher_referred)
    #                 getReferralNotDone= TeachersReferral.objects.filter(status = None, employeeid=user)
    #                 for object1 in getReferralNotDone:
    #                     if object1.studnumber==studentNumber and object1.subject_referred==subject and object1.employeeid==user:
    #                         print(object1.id)
    #                         TeachersReferral.objects.filter(id=object1.id).update(
    #                             start_time=counselorSched[index].time1,end_time=counselorSched[index+1].time2)
                            
    #                 break
    return render(request, "teacher/new.html")


@login_required(login_url='login')
def teacher_view_students(request, id):
    chuchu = list()
    chuchu  = []
    studentslist = []
    print(id)
    qs = Studentsload.objects.filter(offer_no = id)
    for student in qs:
        chuchu.append(Students (student.studnumber))
    qs_student = Students.objects.all()
    print(qs_student.count())
    for stud in qs_student:
        print("baho")
        for chu in chuchu:
            print ("sud")
            if stud.studnumber == chu.studnumber:
               print ("suddddd")
               studentslist.append(Students(stud.studnumber,
               stud.firstname,stud.lastname,stud.email))
    print(studentslist)
    context = {"object_list": studentslist}
    return render(request, "teacher/list_students.html", context)

@login_required(login_url='login')
def teacher_view_referred_students(request, *args, **kwargs):
    user = request.session.get('username')
    qs = TeachersReferral.objects.filter(employeeid = user)
    context = {"object_list": qs}
    return render(request, "teacher/list_referred_students.html", context)

@login_required(login_url='login')
def teacher_coursecard(request, *args, **kwargs):
    user = request.session.get('username')
    qs = Facultyload.objects.filter(employeeid = user)
    context = {"object_list": qs}
    return render(request, "teacher/about.html",)

#teacher

#counselor
@login_required(login_url='login')
def counselor_home_view(request, *args, **kwargs):
    today = date.today()
    ugma = date.today() + timedelta(days=1)
    now = datetime.now()
    day_name=now.strftime("%a")
    adlaw = [day_name]
    days = SubjectOffered.objects.filter(dayofsub=adlaw)
    print("test piiiff sa subject chuchuc")
    print(days)
    counselorSchedulelist = []
    user = request.session.get('username')
    counselorSubject = Facultyload.objects.filter(employeeid = user)
    allSubjects = SubjectOffered.objects.all()
    counselorsss = CounselorSchedule.objects.order_by('schedid')
    couns=CounselorSchedule.objects.all()
    days = SubjectOffered.objects.filter(dayofsub=day_name)
    for object in allSubjects:
        for object1 in counselorSubject:
            if object.offer_no == object1.offer_no and day_name in object.dayofsub:
                print("charooottt")
                counselorSchedulelist.append(SubjectOffered(object.offer_no, 
                object.subject_no,object.subject_title,object.dayofsub,
                object.start_time,object.end_time,object.units))
    for object in counselorSchedulelist:
        for object1 in couns:
            if(object.start_time==object1.time1 or object.end_time==object1.time2):
                CounselorSchedule.objects.filter(schedid=object1.schedid).update(service_offered='CLASS',description=object.offer_no)
    global ihap
    counselor_name = Teachersload.objects.filter(employeeid = user)
    context = {"object_list": counselor_name}
    return render(request, "counselor/counselor_home.html", {"ihap":ihap} and context)


@login_required(login_url='login')
def counselor_view_schedule(request, *args, **kwargs):
    counselors=CounselorSchedule.objects.all()
    context = {"object_list": counselors}
    return render(request, "counselor/schedule.html", context)

@login_required(login_url='login')
def counselor_setSchedule(request, pk):
    counselor = CounselorSchedule.objects.get(time1=pk)
    form = CounselorScheduleForm(instance=counselor)
    objectss= CounselorSchedule.objects.order_by('schedid')
    
    if request.method == "POST":
        print("chuchu")
        form = CounselorScheduleForm(request.POST, instance=counselor)
        if form.is_valid():
            schedid = request.POST['schedid']
            service_offered = request.POST['service_offered']
            description= request.POST['description']
            CounselorSchedule.objects.filter(time1=pk).update(service_offered=service_offered,description=description)
            counselorsss = CounselorSchedule.objects.order_by('schedid')
            context = {"object" : counselorsss}
            return render(request, "counselor/schedule.html",context)
    context = {"form": form}
    return render(request, "counselor/set_schedule.html", context )


@login_required(login_url='login')
def counselor_view_referred_students(request, *args, **kwargs):
    user = request.session.get('username')
    qs = TeachersReferral.objects.filter(counselor = user)
    context = {"object_list": qs}
    return render(request, "counselor/referred_students.html", context)

@login_required
def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)
    extra_id = request.GET.get('extra_id', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.AUTOMATIC_REFERRAL:
            return render(request, "counselor/counselor.html", {})
        elif notification.notification_type == Notification.MANUAL_REFERRAL:
            return render(request, "counselor/counselor.html", {})

    notif = Notification.objects.all()
    return render(request, 'counselor/notification.html', {"notifications":notif})

@login_required
def manual_detail(request, pk, created_by):
    global ihap
    student = TeachersReferral.objects.filter(studnumber=pk, employeeid=created_by)
    if ihap != 0 and ihap > 0:
        ihap-=1
    return render(request, 'counselor/manual_detail.html', {"object":student})

# @login_required
# def approve(request, pk):
#     user = request.session.get('username')
#     # qs = Students.objects.filter(studnumber = pk)
#     # qs_1 = Counselor.objects.filter(program_designation=qs.course)
#     # create_notification(qs_1, user, 'manual_referral', extra_id=int(pk))
#     # # student = TeachersReferral.objects.filter(studnumber=pk, employeeid=created_by)
#     # # if ihap != 0 and ihap > 0:
#     # #     ihap-=1
#     return render(request, 'counselor/approve.html')

#counselor
#  create_notification(couns, user, 'manual_referral', extra_id=int(stdnum))

#student
@login_required(login_url='login')
def student_home_view(request, *args, **kwargs):
    global ihap1
    return render(request, "student/student_home.html", {"ihap1":ihap1})

@login_required(login_url='login')
def student_schedule(request, *args, **kwargs):
    studentSchedulelist = []
    user = request.session.get('username')
    studentSubject = Studentsload.objects.filter(studnumber = user)
    allSubjects = SubjectOffered.objects.all()
    studentssss = StudentSchedule.objects.order_by('schedid')
    stud=StudentSchedule.objects.all()
    for object in allSubjects:
        for object1 in studentSubject:
            if object.offer_no == object1.offer_no:
                studentSchedulelist.append(SubjectOffered(object.offer_no, 
                object.subject_no,object.subject_title,object.dayofsub,
                object.start_time,object.end_time,object.units))
    for object in studentSchedulelist:
        for object1 in stud:
            if(object.start_time==object1.time1 or object.end_time==object1.time2):
                StudentSchedule.objects.filter(schedid=object1.schedid).update(schedule='CLASS',description=object.offer_no)
    context = {"object" : studentssss}
  
    return render(request, "student/schedule.html", context )

@login_required
def notifications_student(request):
    user = request.session.get('username')
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)
    extra_id = request.GET.get('extra_id', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.AUTOMATIC_REFERRAL:
            return render(request, "student/student_home.html", {})
        elif notification.notification_type == Notification.MANUAL_REFERRAL:
            return render(request, "student/student_home", {})

    notif = Notification.objects.filter(extra_id=user)
    return render(request, 'student/notification.html', {"notifications":notif})

@login_required
def student_notif_detail(request, pk):
    global ihap1
    student = TeachersReferral.objects.filter(studnumber=pk)
    if ihap1 != 0 and ihap1 > 0:
        ihap1-=1
    return render(request, 'student/notif_detail.html', {"object":student})
#student
































































def sample (request, pk):
    counselors=CounselorSchedule.objects.filter(id=pk).update(service_offered='jesus')
    context = {"object": counselors}
    return render(request, "counselor/set_schedule.html",context)


#  counselor = CounselorSchedule.objects.get(id=pk)
#     form = CounselorScheduleForm(instance=counselor)
#     form = CounselorScheduleForm(request.POST, instance=counselor)
#     # data = form.cleaned_data
#     # service_offered = data.get("service_offered")
#     # # description = form['description']
#     counselors=CounselorSchedule.objects.filter(id=pk).update(service_offered="service_offer")
  
#     #     form = CounselorScheduleForm(request.POST, instance=counselor)
#     #     if form.is_valid():
#     #         form.save()
#     #         return render(request, "counselor/counselor_home.html")
#     context = {"object": counselors}
#     return render(request, "counselor/set_schedule.html", context )






































@login_required(login_url='login')
def student_view(request, *args, **kwargs):
    return render(request, "students/student.html", {})

@login_required(login_url='login')
def studentRefer_detail_view(request, pk):
    try:
        object = TeachersReferral.objects.get(pk=pk)
    except TeachersReferral.DoesNotExist:
        raise Http404
    # return HttpResponse(f"Product id{obj.pk}")
    return render(request, "students/detail_student.html", {"object": object})

@login_required(login_url='login')
def student_list_view(request, *args, **kwargs):
    return render(request, "students/student_list.html", {})

@login_required(login_url='login')
def about_view(request, *args, **kwargs):
    qs = TeachersReferral.objects.all()
    context = {"object_list": qs}
    return render(request, "students/about.html", context)



# def new(request):
#     if request.method=="POST":
#        print("this is it")
#        firstname= request.POST['firstname']
#        lastname= request.POST['lastname']
#        studid= request.POST['studid']
#        degree_program= request.POST['degree_program']
#        subject_referred= request.POST['subject_referred']
#        reasons= request.POST['reasons']
#        print(firstname,lastname,studid,degree_program,subject_referred,reasons)
#        studentInfo = Teachers(firstname=firstname, lastname=lastname,studid=studid,degree_program = degree_program,subject_referred=subject_referred,reasons=reasons)
#        studentInfo.save()
#     return render(request, "students/new.html")
# @login_required(login_url='login')
# def new(request, *args, **kwargs):
#     form = TeachersReferralForm(request.POST or None)
#     if form.is_valid():
#         print(form.cleaned_data)
#         data = form.cleaned_data
#         TeachersReferral.objects.create(**data)
#         form = TeachersReferralForm
#         print(TeachersReferralForm)
#     return render(request, "students/new.html", {"form": form})

@login_required(login_url='login')
def export_studentslist(request):
    students_resource = TeachersloadResource()
    dataset = students_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="students.xls"'
    return response

@login_required(login_url='login')
def upload_studentslist(request):
    if request.method == 'POST':
        student_resource = TeachersloadResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
           
        	print(data[1])
        	value = Teachersload(
                data[0],
                data[1], 
                data[2], 
                data[3], 
                data[4], 
                )
        	value.save()     
    return render(request, "students/upload.html")

@login_required(login_url='login')
def students_view(request, *args, **kwargs):
    qs = Students.objects.all()
    context = {"object_list": qs}
    return render(request, "students/students_view.html", context)


# def export(request):
#     teacher_resource = TeachersResource()
#     dataset = teacher_resource.export()
#     response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="persons.xls"'
#     return response

# def simple_upload(request):
#     if request.method == 'POST':
#         teacher_resource = TeachersResource()
#         dataset = Dataset()
#         new_students = request.FILES['myfile']

#         imported_data = dataset.load(new_students.read(),format='xlsx')
#         print(imported_data)
#         for data in imported_data:
           
#         	print(data[1])
#         	value = Teachers(
#                 data[0],
#                 data[1], 
#                 data[2], 
#                 data[3], 
#                 data[4], 
#                 data[5], 
#                 )
#         	value.save()     
#     return render(request, "students/upload.html")


# def firstPage(request):
#     print("hhh")
#     if request.method == 'POST':
#         print("a")
#         flag=0
#         usernamee = request.POST.get('usernamee')
#         passwordd = request.POST.get('passwordd')
#         qs = Students.objects.all()
#         print("b")
#         for student in qs:
#             print("c")
#             print(student.studnumber)
#             if student.studnumber == usernamee:
#                 flag = 1
#         print("d")
#         if flag == 1:
#             print("one")
#             return redirect('register')
#         else:
#            print("two")
#            return render(request, 'firstpage.html',)
#     return render(request, 'firstpage.html',)

# def registerPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, 'Account was created for ' + user)
# 			return redirect('login')
# 	return render(request, 'register.html', {'form':form})

# def loginPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password = request.POST.get('password')

# 			user = authenticate(request, username=username, password=password)

# 			if user is not None:
# 				login(request, user)
# 				return redirect('home')
# 			else:
# 				messages.info(request, 'Username OR password is incorrect')

# 		return render(request, 'login.html', {})