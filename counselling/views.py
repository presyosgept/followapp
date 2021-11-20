from json import encoder
from typing import Counter
from django.db.models.fields import TimeField
from django.http import HttpResponse, request
from django.http.response import Http404
from django.shortcuts import render, redirect 
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .utilities import create_notification,create_feedback
from django.views import generic
from django.utils import timezone
from datetime import date,datetime,timedelta

import datetime as dt

from .forms import OfferingForm,StudentSetSchedForm,CounselorFeedbackForm,VerificationForm,AccountCreatedForm,AccountsForm,CounselorForm, TeachersReferralForm, StudentsForm,CreateUserForm, SubjectOfferedForm, FacultyloadForm, StudentsloadForm
from .models import  Offering,StudentSetSched,NotificationFeedback,CounselorFeedback,SubjectWithSem,Semester,AccountCreated,Faculty,Counselor,Notification,Counselor,TeachersReferral,  SubjectOffered, Facultyload, Studentsload

from .resources import SubjectWithSemResource,SemesterResource,StudentsloadResource,FacultyResource,CounselorResource,TeachersReferralResource, SubjectOfferedResource,FacultyloadResource
from tablib import Dataset

# Create your views here.

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import FacultySerializers,ResultSerializer, Result, UserSerializer

from .models import  AccountsApi,AllSubject,OfferCode,SchoolOffices,Department,DegreeProgram,AllStudent,AllFaculty

from .resources import AllSubjectResource,OfferCodeResource,SchoolOfficesResource,DepartmentResource,DegreeProgramResource,AllStudentResource,AllFacultyResource
import openpyxl


from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.core.mail import get_connection
from django.core.mail.message import EmailMessage
import random

from .serializers import UserSerializer,ActorSerializer,Actor
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view

 
# Create your views here.

# class studentsList(APIView):
#     def get(self, request):
#         stud = Students.objects.all()
#         serializer=studentsSerializers(stud, many=True)
#         return Response({'students':serializer.data})

class CounselorList(APIView):
    def get(self, request):
        # couns = Faculty.objects.all()
        # serializer=FacultySerializers(couns, many=True)
        obj = Result(bool1 = True)
        serializer = ResultSerializer(obj)
        return Response(serializer.data)

#api

class RegisterApi(APIView):
    def get(self, request, id, email):
        char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        for x in range(0,1):
            code=''
            for x in range(0,8):
                code_char = random.choice(char)
                code = code + code_char

        userTeacher = Faculty.objects.filter(employee_id=id).first()
        userStudent = AllStudent.objects.filter(studnumber=id).first()
        exist = AccountsApi.objects.filter(id_number=id).first()
        flag=0
        if exist is not None:
            flag = 1
        obj = Result(bool1 = False)
        if userTeacher is not None or userStudent is not None:
            if flag == 0:
                connection = get_connection(use_tls=True,
                host='smtp.gmail.com', 
                port=587,
                username='followapp2021@gmail.com', 
                password='followapp#123')
                EmailMessage(
                        "Verification Code", 
                        "This is your verification code: " + code, 
                        'followapp2021@gmail.com', 
                [
                    email,
                ], connection=connection).send()
                value = AccountsApi(id_number=id, email=email, code=code)
                value.save()
                obj = Result(bool1 = True)
                serializer = ResultSerializer(obj)
                return JsonResponse({"result": "Account Created"}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"result": "Account is Existing"},status=status.HTTP_400_BAD_REQUEST)


        serializer = ResultSerializer(obj)
        return JsonResponse({"result": "Invalid Account"},status=status.HTTP_400_BAD_REQUEST)


        
class VerificationApi(APIView):
    def get(self, request, id, code):
        user = AccountsApi.objects.filter(id_number=id, code=code).first()
        obj = Result(bool1 = False)
        if user is not None:
            obj = Result(bool1 = True)
            serializer = ResultSerializer(obj)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = ResultSerializer(obj)
            return JsonResponse(serializer.data,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST', 'DELETE'])
def signup_api(request):
        if request.method == 'POST':
            user_data = JSONParser().parse(request)
            user_serializer = UserSerializer(data=user_data)
         
        username = str(user_data["username"])
        user = AccountsApi.objects.filter(id_number=username).first()
        if user_serializer.is_valid():
            if user is not None:
                user_serializer.save()
                return JsonResponse(user_serializer.data, status=status.HTTP_200_OK) 
            else:
                return JsonResponse({"username": "Username Not Valid"}, status=status.HTTP_400_BAD_REQUEST) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def login_api(request):
        if request.method == 'POST':
            user_data = JSONParser().parse(request)

        username = str(user_data["username"])
        password = str(user_data["password"])
        user = User.objects.filter(username=username, password=password).first()
        userTeacher = Faculty.objects.filter(employee_id=username).first()
        userStudent = AllStudent.objects.filter(studnumber=username).first()
        
        if user is not None:
            if userTeacher is not None:
                obj = Actor(actor = "teacher")
                serializer = ActorSerializer(obj)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            if userStudent is not None:
                obj = Actor(actor = "learner")
                serializer = ActorSerializer(obj)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'actor':"no account"},status=status.HTTP_400_BAD_REQUEST)



# couns = Faculty.objects.all()
        # serializer=FacultySerializers(couns, many=True)
# ({'students':serializer.data})

# from django.contrib.auth.forms import User
# class RegisterApi(APIView):
#     def get(request, id, password):
#         user = User.objects.create(
#                 username=id,
#                 password = password
#             )
#         user.save()
#         return user
#         # obj = Result(bool1 = False)
#         # accs = AccountsApi.objects.all()
#         # for check in accs:
#         #     if(check.id_number == id):
#         #         user = authenticate(request, username=id, password=password)
#         #         obj = Result(bool1 = True)

#         # serializer = ResultSerializer(obj)
#         # return Response(serializer.data)

#     # def create(self, validated_data):
            
#api








notif = 0
notif1 =0
notif2 =0
formm = AccountsForm()

def register(request):
    form = AccountCreatedForm()
    if request.method == 'POST':
        char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        for x in range(0,1):
            code=''
            for x in range(0,8):
                code_char = random.choice(char)
                code = code + code_char
        username = request.POST.get('id_number')
        email = request.POST.get('email')
        qs_faculty = Faculty.objects.all()
        qs_student = AllStudent.objects.all()
        qs_acc = AccountCreated.objects.all()

        if username == 'followapp':
            connection = get_connection(use_tls=True,
            host='smtp.gmail.com', 
            port=587,
            username='followapp2021@gmail.com', 
            password='followapp#123')
            EmailMessage(
                "Verification Code", 
                "This is your verification code: " + code, 
                'followapp2021@gmail.com', 
            [
                email,
            ], connection=connection).send()
            value = AccountCreated(id_number=username,email=email, password=code)
            value.save()
            return redirect('verification_code')

        exist = 0
        for acc in qs_acc:
            if username == acc.id_number:
                exist=1

        if exist == 0:
            flag = 0
            for user in qs_student:
                if username == user.studnumber:
                    flag=1
            for user in qs_faculty:
                if username == user.employee_id:
                    flag=1
            if flag == 1:
                connection = get_connection(use_tls=True,
                host='smtp.gmail.com', 
                port=587,
                username='followapp2021@gmail.com', 
                password='followapp#123')
                EmailMessage(
                    "Verification Code", 
                    "This is your verification code: " + code, 
                    'followapp2021@gmail.com', 
                [
                    email,
                ], connection=connection).send()
                value = AccountCreated(id_number=username,email=email, password=code)
                value.save()
                messages.info(request, "Check Gmail for Code")
                return redirect('verification_code')
            else:
                messages.info(request, "Account Not Valid")
        else:
            messages.info(request, "Account Already Existing")
    else:
        AccountsForm()
        

    return render(request,'register.html',{'form':form})

def verification_code(request):
    form = VerificationForm()
    code = request.POST.get('code')
    if request.method == 'POST':
        qs_account = AccountCreated.objects.all()
        flag=0
        for vcode in qs_account:
            if (code == vcode.password):
                flag=1
        
        if(flag==1):
            return redirect('signup')
        else:
            VerificationForm()
            messages.info(request, 'Invalid Code')
    else:
        VerificationForm()

    return render(request, 'verification.html', {'form':form})


def signup(request):
	if request.user.is_authenticated:
		return redirect('login')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
                    username = request.POST.get('username')
                    qs_account = AccountCreated.objects.all()
                    exist = 0
                    for user in qs_account:
                        if user.id_number == username:
                            exist =1
                    print("yeeeeeee")
                    print(exist)
                    if (exist == 1):
                        flag = 0
                        qs = AllStudent.objects.all()
                        for student in qs:
                            if student.studnumber ==username:
                                flag = 1
                        if flag == 1:
                            form = CreateUserForm(request.POST)
                            if form.is_valid():
                                form.save()
                                user = form.cleaned_data.get('username')
                                messages.info(request, 'Student Account was created for ' + user)
                                return redirect('login')
                        elif flag == 0:
                            qs = Faculty.objects.all()
                            for teacher in qs:
                                if teacher.employee_id == username:
                                    form = CreateUserForm(request.POST)
                                    if form.is_valid():
                                        form.save()
                                        user = form.cleaned_data.get('username')
                                        messages.info(request, 'Account was created for ' + user)
                                        return redirect('login')
                            
                        if username == 'followapp':
                            form = CreateUserForm(request.POST)
                            if form.is_valid():
                                form.save()
                                user = form.cleaned_data.get('username')
                                messages.info(request, 'Admin Account was created for ' + user)
                                return redirect('login')

                        messages.info(request, 'Check Credentials Account Not Created')
                    
                    else:
                        messages.info(request, 'Check Credentials Account Not Created')  
    
	return render(request, 'signup.html', {'form':form})

def loginPage(request):
	if request.user.is_authenticated:
            return redirect('login')    
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
                                    qs = AllStudent.objects.all()
                                    for student in qs:
                                        if student.studnumber == username:
                                            if student.role == 'learner':
                                                flag = 1
                                    if flag == 1:
                                        request.session['username'] = username
                                        return redirect('student_home_view')
                                    else:
                                        qs = Faculty.objects.all()
                                        for teacher in qs:
                                            if teacher.employee_id ==username:
                                                if teacher.role == 'teacher':
                                                        request.session['username'] = username
                                                        flag = 2
                                                elif teacher.role == 'counselor':
                                                        request.session['username'] = username
                                                        flag = 3
                                                elif teacher.role == 'director':
                                                        request.session['username'] = username
                                                        flag = 4
                                    if flag == 2:
                                            return redirect('teacher_home_view')
                                    if flag == 3:
                                            return redirect('counselor_home_view')
                                    if flag == 4:
                                        return redirect('director_home_view')
                                    if username == 'followapp':
                                        return redirect('admin_home_view')
                                    if username == 'upload':
                                        return redirect('uploaddb_home_view')
                                    
			else:
				messages.info(request, 'Username or Password is Incorrect')

		return render(request, 'login.html', {})



def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request, *args, **kwargs):
    return render(request, "welcomepage.html", {})


#director
@login_required(login_url='login')
def director_home_view(request, *args, **kwargs):
    user = request.session.get('username')
    director_name = Faculty.objects.filter(employee_id = user)
    return render(request, "director/director_home.html", {"form" :director_name})

@login_required(login_url='login')
def director_assign_counselor(request, *args, **kwargs):
    user = request.session.get('username')
    director_name = Faculty.objects.filter(employee_id = user)
    qs = Faculty.objects.filter(role='counselor')
    return render(request, "director/assign_counselor.html", {"object_list": qs,"form" :director_name})

@login_required(login_url='login')
def director_fillinForm(request, pk):
    counselor = Counselor.objects.get(employee_id=pk)
    form = CounselorForm(instance=counselor)
    qs = Faculty.objects.filter(role='counselor')
    context = {"object_list": qs}
    if request.method == "POST":
        form = CounselorForm(request.POST, instance=counselor)
        if form.is_valid():
            form.save()
            return render(request, "director/assign_counselor.html", context)
    context = {"form": form}
    user = request.session.get('username')
    director_name = Faculty.objects.filter(employee_id = user)
    return render(request, "director/form.html",{"form1": form,"form" :director_name})

#director


#admin
@login_required(login_url='login')
def admin_home_view(request, *args, **kwargs):
    tomorrow = date.today() + timedelta(days=1)
    print(str(tomorrow))
    return render(request, "admin/admin_home.html", {})

@login_required(login_url='login')
def admin_offering(request, *args, **kwargs):
    form = OfferingForm()
    if request.method == "POST":
        form = OfferingForm(request.POST)
        if form.is_valid():
            form.save()
            semester = form['semester'].value()
            schoolyear = form['school_year'].value()
            return admin_view_offering(request, semester, schoolyear)

    return render(request, "admin/offering.html", {"form" : form})

@login_required(login_url='login')
def admin_view_offering(request, semester, schoolyear):
    print("semseter " + str(semester))
    print("schoolyear " + str(schoolyear))
    sem = ''
    if semester == "1ST SEM": 
        sem = "101"
    elif semester == "2ND SEM": 
        sem = "201"

    print(sem)
    qs = OfferCode.objects.filter(sem_id = sem , academic_year = schoolyear )
    return render(request, "admin/viewoffering.html", {"forms" : qs})


@login_required(login_url='login')
def upload_studentsload(request):
    if request.method == 'POST':
        StudentsloadResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        wb_obj = openpyxl.load_workbook(new_students)
        sheet_obj = wb_obj.active
        col = sheet_obj.max_column
        row = sheet_obj.max_row

        if(col == 3):
            for data in imported_data:
                value = Studentsload(
                    data[0],
                    data[1], 
                    data[2],   
                    )
                value.save()   
            messages.info(request, 'Successfully Added')
        else:
            messages.info(request, 'Failed to Add the Data')
    else:
        messages.info(request, 'No data has been added Yet')    
    return render(request, "admin/upload_studentsload.html")


@login_required(login_url='login')
def upload_students(request):
    if request.method == 'POST':

        AllStudentResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']
        imported_data = dataset.load(new_students.read(),format='xlsx')
        wb_obj = openpyxl.load_workbook(new_students)
        sheet_obj = wb_obj.active
        col = sheet_obj.max_column
        row = sheet_obj.max_row
        if(col == 8):
                for data in imported_data:
                        value = AllStudent(
                            data[0],
                            data[1], 
                            data[2],
                            data[3],
                            data[4], 
                            data[5],
                            data[6],
                            data[7],
                            )
                        value.save()  
                messages.info(request, 'Successfully Added')
        else:
            messages.info(request, 'Failed to Add the Data')
    else:
        messages.info(request, 'No data has been added Yet')  
    return render(request, "admin/upload_students.html")


@login_required(login_url='login')
def upload_faculty(request):
    if request.method == 'POST':
        FacultyResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        wb_obj = openpyxl.load_workbook(new_students)
        sheet_obj = wb_obj.active
        col = sheet_obj.max_column
        row = sheet_obj.max_row

        
        if(col == 5):
            for data in imported_data:
                value = Faculty(
                    data[0],
                    data[1], 
                    data[2], 
                    data[3], 
                    data[4], 
                    )
                value.save()
            messages.info(request, 'Successfully Added')
        else:
            messages.info(request, 'Failed to Add the Data')
    else:
        messages.info(request, 'No data has been added Yet')     
    return render(request, "admin/upload_faculty.html")

@login_required(login_url='login')
def upload_facultyload(request):
    if request.method == 'POST':
        FacultyloadResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        wb_obj = openpyxl.load_workbook(new_students)
        sheet_obj = wb_obj.active
        col = sheet_obj.max_column
        row = sheet_obj.max_row

        if(col == 3):
            for data in imported_data:
                value = Facultyload(
                    data[0],
                    data[1], 
                    data[2],
                    )
                value.save()
            messages.info(request, 'Successfully Added')
        else:
            messages.info(request, 'Failed to Add the Data')
    else:
        messages.info(request, 'No data has been added Yet')     
    return render(request, "admin/upload_facultyload.html")



#admin

#teacher
@login_required(login_url='login')
def teacher_home_view(request, *args, **kwargs):
    user = request.session.get('username')
    user_name = Faculty.objects.filter(employee_id = user)
    fload = Facultyload.objects.filter(employee_id = user)

    # studentReferred //student id of t the student referred
    global notif2
    
  
    return render(request, "teacher/teacher_home.html",  {"object_list": fload,"notif2": notif2,"form": user_name} )

@login_required(login_url='login')
def new(request,stud,id):
    global notif
    global notif1
    time1 = ""
    time2 = ""
    subj = OfferCode.objects.get(offer_code=id)
    user = request.session.get('username')
    user_name = Faculty.objects.filter(employee_id = user)
    studentReferred = AllStudent.objects.get(studnumber=stud)
    subject_referred = subj.subject_code
    form = TeachersReferralForm(instance=studentReferred, initial={'subject_referred': subject_referred })

    qs = Facultyload.objects.filter(employee_id = user)
    context = {"object_list": qs}
    degree = DegreeProgram.objects.get(program_id = studentReferred.degree_program_id)
    if request.method == "POST":
        reasons= request.POST['reasons']
        behavior= request.POST['behavior_problem']
        form = TeachersReferralForm(request.POST, instance=studentReferred,initial={'subject_referred': subject_referred })
        if form.is_valid():
            today = date.today()
            now = dt.datetime.now()
            ClassesofCounselor=[]
            ClassesCounselor = []
            tomorrow=today
            finder=0
            
            counselor = Counselor.objects.get(program_designation = degree.program_code)
            OfferCodeCounselor = Facultyload.objects.filter(employee_id = counselor.employee_id)
            
            timeArray = [] 
            initialtime = 0

            newTime = str(initialtime)+':00:00'

            for x in range(24):
                    timeArray.append(datetime.strptime(newTime, '%H:%M:%S').time())
                    newTime = str(initialtime)+':30:00'  
                    timeArray.append(datetime.strptime(newTime, '%H:%M:%S').time())
                    initialtime = initialtime + 1   
                    newTime = str(initialtime)+':00:00'

            while(finder==0):
                tomorrow=tomorrow+timedelta(days=1)
                day_name=tomorrow.strftime("%a")
                ScheduledReferralbyDay = TeachersReferral.objects.filter(date=tomorrow)
                OfferCodeCounselorCheck=bool(OfferCodeCounselor)
                ScheduledReferralbyDayCheck = bool(ScheduledReferralbyDay)
                if(ScheduledReferralbyDayCheck == True):
                    ScheduledReferralbyDayCheck= True
                else:
                    ScheduledReferralbyDayCheck= False
                if(OfferCodeCounselorCheck==True):
                        for object in OfferCodeCounselor:
                            Subject=OfferCode.objects.get(offer_code=object.offer_code_id)
                            ClassesofCounselor.append(Subject)
                        for object in ClassesofCounselor:
                            for d in object.days:
                                if d == day_name:
                                    ClassesCounselor.append(OfferCode(offer_code = object.offer_code,days = object.days,
                                    start_time= object.start_time,end_time= object.end_time,room = object.room,
                                    subject_code = object.subject_code,sem_id=object.sem_id, academic_year = object.academic_year,))
                        ClassesCounselorCheck = bool(ClassesCounselor)    
                else:
                    ClassesCounselorCheck=False

                start = datetime.strptime('8:00:00', '%H:%M:%S').time()
                end = datetime.strptime('17:00:00', '%H:%M:%S').time()
                        
                

                TimeTaken=0
                TimeTaken1=0
                counter=0

                if (ClassesCounselorCheck==False and ScheduledReferralbyDayCheck ==False):
                        startTime =datetime.strptime('8:00:00', '%H:%M:%S').time()
                        endTime =datetime.strptime('9:00:00', '%H:%M:%S').time()
                        time1=startTime
                        time2=endTime
                        finder=1     
                elif(ClassesCounselorCheck==False and ScheduledReferralbyDayCheck ==True):
                            for x in range(len(timeArray)):
                                if(timeArray[x] >= start and timeArray[x] < end):
                                    for object2 in ScheduledReferralbyDay:
                                        if(timeArray[x+1]<=object2.end_time and timeArray[x]>=object2.start_time):
                                            TimeTaken+=1
                                            
                                    if(TimeTaken==0 and counter==0):
                                        time1=timeArray[x]
                                        counter=1
                                        TimeTaken=0;	
                                    elif(TimeTaken==0 and counter==1):
                                        time2=timeArray[x+1]
                                        counter=0
                                        finder=1
                                        break
                                    elif(TimeTaken!=0):
                                        time1=''
                                        TimeTaken=0

                elif(ClassesCounselorCheck==True and ScheduledReferralbyDayCheck ==False):
                        for x in range(len(timeArray)):
                                if(timeArray[x] >= start and timeArray[x] < end):
                                    for object2 in ClassesCounselor:
                                            if(timeArray[x+1]<=object2.end_time and timeArray[x]>=object2.start_time):
                                                TimeTaken+=1
                                    if(TimeTaken==0 and counter==0):
                                        time1=timeArray[x]
                                        counter=1
                                        TimeTaken=0;	
                                    elif(TimeTaken==0 and counter==1):
                                        time2=timeArray[x+1]
                                        counter=0
                                        TimeTaken=0
                                        finder=1
                                        break
                                    elif(TimeTaken!=0):
                                        time1=''
                                        TimeTaken=0
                elif(ClassesCounselorCheck==True and ScheduledReferralbyDayCheck ==True):
                        for x in range(len(timeArray)):
                            if(timeArray[x] >= start and timeArray[x] < end):
                                for object2 in ScheduledReferralbyDay:
                                    if(timeArray[x+1]<=object2.end_time and timeArray[x]>=object2.start_time):
                                        TimeTaken+=1
                                if(TimeTaken==0):
                                    for object3 in ClassesCounselor:
                                        if(timeArray[x+1]<=object3.end_time and timeArray[x]>=object3.start_time):
                                            TimeTaken1+=1
                                    if(TimeTaken1==0 and counter==0):
                                        time1=timeArray[x]
                                        counter=1
                                        TimeTaken=0	
                                        TimeTaken1=0
                                    elif (TimeTaken1==0 and counter==1):
                                        time2=timeArray[x+1]
                                        finder=1
                                        counter=0
                                        TimeTaken=0	
                                        TimeTaken1=0
                                        break
                                    elif(TimeTaken1!=0):
                                        time1=''
                                        TimeTaken=0
                                        TimeTaken1=0
                                        counter=0
                                            
                                else:
                                    counter=0
                                    TimeTaken=0
                                    time1=''
                            else:
                                counter=0
                                TimeTaken=0
                                time1='' 
                ScheduledReferralbyDay=[]
                ClassesCounselor=[]

            if(time1!='' and time2!=''):
                form.save()
                qs = Counselor.objects.get(program_designation = degree.program_code)
                studentInfo = TeachersReferral(firstname=studentReferred.firstname, 
                lastname=studentReferred.lastname,studnumber=studentReferred.studnumber,
                degree_program = degree.program_code,subject_referred=subject_referred,
                reasons=reasons,counselor=qs.employee_id,employeeid=user,behavior_problem = behavior, start_time = time1 , end_time = time2, date = tomorrow )
                studentInfo.save()
                form = TeachersReferralForm(instance=studentReferred,initial={'subject_referred': subject_referred })
                context = {"form1": form,"form":user_name}
                notif = notif + 1 
                notif1 = notif1 + 1
                create_notification(qs.employee_id, user, 'manual_referral', extra_id=int(stud), schedDay = tomorrow , schedStartTime = time1 , schedEndTime = time2)
                messages.info(request, 'Successfully Referred the Student')
                print("eeeeeeeee")

    context = {"form1": form,"form":user_name}
    return render(request, "teacher/new.html", context )





@login_required(login_url='login')
def teacher_view_students(request, id):
    chuchu = list()
    chuchu  = []
    studentslist = []
    finalstudentlist=[]
    qs = Studentsload.objects.filter(offer_code = id)
    for std in qs:
        chuchu.append(AllStudent(std.studnumber_id))

    qs_student = AllStudent.objects.all()
    for stud in qs_student:
        for chu in chuchu:
            if stud.studnumber == chu.studnumber:
               studentslist.append(AllStudent(stud.studnumber,stud.email))
   
    allstud = AllStudent.objects.all()
    for allstud in allstud:
        for stud in studentslist:
            if allstud.studnumber == stud.studnumber:
                finalstudentlist.append(AllStudent(allstud.studnumber,allstud.firstname,allstud.lastname))
    user = request.session.get('username')
    user_name = Faculty.objects.filter(employee_id = user)
    return render(request, "teacher/list_students.html", {"id": id,"object_list": finalstudentlist,"form": user_name})

@login_required(login_url='login')
def teacher_view_referred_students(request, *args, **kwargs):
    user = request.session.get('username')
    qs = TeachersReferral.objects.filter(employeeid = user)
    user = request.session.get('username')
    user_name = Faculty.objects.filter(employee_id = user)
    return render(request, "teacher/list_referred_students.html", {"object_list": qs,"form": user_name})

@login_required(login_url='login')
def teacher_view_detail_referred_students(request, id):
    user = request.session.get('username')
    detail=[]
    qs = TeachersReferral.objects.filter(employeeid = user)
    for referedStud in qs:
        if(referedStud.id==id):
            detail.append(TeachersReferral(firstname=referedStud.firstname, 
            lastname=referedStud.lastname,studnumber=referedStud.studnumber,
            degree_program = referedStud.degree_program,subject_referred=referedStud.subject_referred,
            reasons=referedStud.reasons,behavior_problem = referedStud.behavior_problem))
    user = request.session.get('username')
    user_name = Faculty.objects.filter(employee_id = user)
    return render(request, "teacher/modal.html", {"object_list": detail,"form": user_name})


@login_required(login_url='login')
def teacher_coursecard(request, *args, **kwargs):
    user = request.session.get('username')
    qs = Facultyload.objects.filter(employee_id = user)
    context = {"object_list": qs}
    return render(request, "teacher/about.html",)


@login_required
def notifications_teacher(request):
    user = request.session.get('username')
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)
    extra_id = request.GET.get('extra_id', 0)

    if goto != '':
        notification = NotificationFeedback.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        if notification.notification_type == NotificationFeedback.AUTOMATIC_REFERRAL:
            return render(request, "teacher/counselor.html", {})
        elif notification.notification_type == NotificationFeedback.MANUAL_REFERRAL:
            return render(request, "teacher/counselor.html", {})

    notif = NotificationFeedback.objects.filter(to_user = user)
    counselor_name = Faculty.objects.filter(employee_id = user)
    return render(request, 'teacher/notification.html', {"notifications":notif,"form": counselor_name} )

@login_required(login_url='login')
def teacher_view_notif_detail(request, id):
    global notif2
    user = request.session.get('username')
    detail = []
    fback = CounselorFeedback.objects.get(id=id)
    notif = NotificationFeedback.objects.get(id=id)
    students = TeachersReferral.objects.all()
    for referedStud in students:
        if notif.extra_id == referedStud.id:
            detail.append(TeachersReferral(firstname=referedStud.firstname, 
            lastname=referedStud.lastname,studnumber=referedStud.studnumber,
            degree_program = referedStud.degree_program, subject_referred=referedStud.subject_referred,feedback = fback.feedback))
    user_name = Faculty.objects.filter(employee_id = user)
    if notif2 != 0:
        notif2 = notif2 - 1
    return render(request, "teacher/detailNotif.html", {"objects": detail,"form": user_name})



#teacher

#counselor
@login_required(login_url='login')
def counselor_home_view(request, *args, **kwargs):
    # today = date.today()
    # tomorrow=today
    # i=0
    # print("pifff")
    # for i in range(3): 
    #     tomorrow=tomorrow+timedelta(days=1)
    #     print("pifff")
    #     print(tomorrow)
    # today = date.today()
    # ugma = date.today() + timedelta(days=1)
    # now = datetime.now()
    # day_name=now.strftime("%a")
    # adlaw = [day_name]
    # days = SubjectOffered.objects.filter(dayofsub=adlaw)
    # print("test piiiff sa subject chuchuc")
    # print(days)
    # counselorSchedulelist = []
    user = request.session.get('username')
    # counselorSubject = Facultyload.objects.filter(employee_id = user)
    # allSubject = SubjectOffered.objects.all()
    # counselorsss = CounselorSchedule.objects.order_by('schedid')
    # couns=CounselorSchedule.objects.all()
    # days = SubjectOffered.objects.filter(dayofsub=day_name)
    # for object in allSubject:
    #     for object1 in counselorSubject:
    #         if object.offer_no == object1.offer_no and day_name in object.dayofsub:
    #             print("charooottt")
    #             counselorSchedulelist.append(SubjectOffered(object.offer_no, 
    #             object.subject_no,object.subject_title,object.dayofsub,
    #             object.start_time,object.end_time,object.units))
    # for object in counselorSchedulelist:
    #     for object1 in couns:
    #         if(object.start_time==object1.time1 or object.end_time==object1.time2):
    #             CounselorSchedule.objects.filter(schedid=object1.schedid).update(service_offered='CLASS',description=object.offer_no)
    global notif
    counselor_name = Faculty.objects.filter(employee_id = user)
    return render(request, "counselor/counselor_home.html", {"notif":notif,"form": counselor_name})


@login_required(login_url='login')
def counselor_view_schedule(request, *args, **kwargs):
    user = request.session.get('username')
    today = date.today()
    now = dt.datetime.now()
    day_name=now.strftime("%a")
    getsched = []
    classForToday = []
    getScheduleToday = TeachersReferral.objects.filter(date=today)
    getappointmentToday = StudentSetSched.objects.filter(date=today)
    
    getFacultyload = Facultyload.objects.filter(employee_id = user)  
    getOffercode = OfferCode.objects.all() 
    for fl in getFacultyload: 
        for oc in getOffercode: 
            if fl.offer_code_id == oc.offer_code:
                getsched.append(OfferCode(offer_code = oc.offer_code,days = oc.days,
                start_time= oc.start_time,end_time= oc.end_time,room = oc.room,
                subject_code = oc.subject_code,sem_id=oc.sem_id, academic_year = oc.academic_year))
    for sched in getsched:
        for d in sched.days:
            if d == day_name:
                classForToday.append(OfferCode(offer_code = sched.offer_code,days = sched.days,start_time= sched.start_time,end_time= sched.end_time,room = sched.room,
                subject_code = sched.subject_code,sem_id=sched.sem_id, academic_year = sched.academic_year))
    print("schedduukkeee")
    print(classForToday)
    counselor_name = Faculty.objects.filter(employee_id = user)
    return render(request, "counselor/schedule.html", {"obj":getappointmentToday,"object":classForToday,"object_list":getScheduleToday,"form": counselor_name})

@login_required(login_url='login')
def counselor_setSchedule(request, pk):
    user = request.session.get('username')
    counselor_name = Faculty.objects.filter(employee_id = user)
    return render(request, "counselor/set_schedule.html",{"form": counselor_name})

@login_required(login_url='login')
def counselor_view_appointment(request, id):
    user = request.session.get('username')
    counselor_name = Faculty.objects.filter(employee_id = user)
    getappointmentToday = StudentSetSched.objects.get(id = id)
    return render(request, "counselor/appointment.html",{"object":getappointmentToday,"form": counselor_name})

@login_required(login_url='login')
def counselor_detail_schedule_counseling(request, id):
    user = request.session.get('username')
    counselor_name = Faculty.objects.filter(employee_id = user)
    session = TeachersReferral.objects.get(id=id)
    return render(request, "counselor/modalCounseling.html", {"object": session, "form": counselor_name})

@login_required(login_url='login')
def counselor_detail_schedule_class(request, offer_code, sem_id, year, ):
    user = request.session.get('username')
    counselor_name = Faculty.objects.filter(employee_id = user)
    session = OfferCode.objects.get(offer_code=offer_code, sem_id=sem_id, academic_year=year)
    return render(request, "counselor/modalClass.html", {"object": session, "form": counselor_name})

@login_required(login_url='login')
def counselor_view_detail_referred_students(request, id):
    global notif
    user = request.session.get('username')
    detail=[]
    qs = TeachersReferral.objects.filter(counselor = user)
    for referedStud in qs:
        if(referedStud.id == id):
            detail.append(TeachersReferral(id = id,firstname=referedStud.firstname, 
            lastname=referedStud.lastname,studnumber=referedStud.studnumber,
            degree_program = referedStud.degree_program,subject_referred=referedStud.subject_referred,
            reasons=referedStud.reasons,behavior_problem = referedStud.behavior_problem, date =referedStud.date, 
            start_time =referedStud.start_time, end_time =referedStud.end_time))
    user_name = Faculty.objects.filter(employee_id = user)
    if notif != 0:
        notif = notif - 1
    return render(request, "counselor/modalC.html", {"objects": detail,"form": user_name})


@login_required(login_url='login')
def counselor_view_referred_students(request, *args, **kwargs):
    user = request.session.get('username')
    qs = TeachersReferral.objects.filter(counselor = user, status = "done")
    counselor_name = Faculty.objects.filter(employee_id = user)
    return render(request, "counselor/referred_students.html", {"objects": qs,"form": counselor_name})
 

@login_required(login_url='login')
def counselor_view_pending_students(request, *args, **kwargs):
    user = request.session.get('username')
    qs = TeachersReferral.objects.filter(counselor = user, status = "pending")
    counselor_name = Faculty.objects.filter(employee_id = user)
    return render(request, "counselor/pending_students.html", {"objects": qs,"form": counselor_name})
 

@login_required(login_url='login')
def counselor_feedback(request,id):
    global notif2
    user = request.session.get('username')
    counselor_name = Faculty.objects.filter(employee_id = user)
    info = Notification.objects.get(id=id)
    student = TeachersReferral.objects.get(id=id)
    referredby = Faculty.objects.get(employee_id = student.employeeid)
    preparedby = Faculty.objects.get(employee_id = student.counselor)
    form1 = CounselorFeedbackForm()
    if request.method == "POST":
        form1 = CounselorFeedbackForm(request.POST)
        if form1.is_valid():
            form1.save()
            form1 = CounselorFeedbackForm()
            create_feedback(student.employeeid,'manual_referral', user, int(id))
            messages.info(request, 'Successfully Feedback')
            notif2 = notif2 + 1 
            t = TeachersReferral.objects.get(id=id)
            t.status = "done"
            t.save()
            return render(request, "counselor/feedback.html", {"info": info,  "info1": referredby,"info2" : preparedby,   "student": student,"object": form1,"form": counselor_name})
                                    
            
    return render(request, "counselor/feedback.html", {"info": info, "info1": referredby,"info2" : preparedby,"student": student,"object": form1,"form": counselor_name})
 


@login_required
def notifications(request):
    user = request.session.get('username')
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

    notif = Notification.objects.filter(to_user = user)
    counselor_name = Faculty.objects.filter(employee_id = user)
    return render(request, 'counselor/notification.html', {"notifications":notif,"form": counselor_name} )


# student
@login_required(login_url='login')
def student_home_view(request, *args, **kwargs):
    global notif1
    
    user = request.session.get('username')
    student_name = AllStudent.objects.filter(studnumber = user)
    return render(request, "student/student_home.html", {"notif1":notif1,"form": student_name})

@login_required(login_url='login')
def student_schedule(request, *args, **kwargs):
    global notif
    global notif1
    user = request.session.get('username')
    student_name = AllStudent.objects.get(studnumber = user)
    schedForm = StudentSetSchedForm(instance=student_name)
    degree = DegreeProgram.objects.get(program_id = student_name.degree_program_id)
    if request.method == "POST":
        reasons= request.POST['reasons']
        schedForm = StudentSetSchedForm(request.POST, instance=student_name)
        if schedForm.is_valid():
            today = date.today()
            now = dt.datetime.now()
            ClassesofCounselor=[]
            ClassesCounselor = []
            tomorrow=today
            finder=0
            
            counselor = Counselor.objects.get(program_designation = degree.program_code)
            OfferCodeCounselor = Facultyload.objects.filter(employee_id = counselor.employee_id)
            timeArray = [] 
            initialtime = 0

            newTime = str(initialtime)+':00:00'

            for x in range(24):
                    timeArray.append(datetime.strptime(newTime, '%H:%M:%S').time())
                    newTime = str(initialtime)+':30:00'  
                    timeArray.append(datetime.strptime(newTime, '%H:%M:%S').time())
                    initialtime = initialtime + 1   
                    newTime = str(initialtime)+':00:00'

            while(finder==0):
                tomorrow=tomorrow+timedelta(days=1)
                day_name=tomorrow.strftime("%a")
                ScheduledReferralbyDay = TeachersReferral.objects.filter(date=tomorrow)
                OfferCodeCounselorCheck=bool(OfferCodeCounselor)
                ScheduledReferralbyDayCheck = bool(ScheduledReferralbyDay)
                if(ScheduledReferralbyDayCheck == True):
                    ScheduledReferralbyDayCheck= True
                else:
                    ScheduledReferralbyDayCheck= False
                if(OfferCodeCounselorCheck==True):
                        for object in OfferCodeCounselor:
                            Subject=OfferCode.objects.get(offer_code=object.offer_code_id)
                            ClassesofCounselor.append(Subject)
                        for object in ClassesofCounselor:
                            for d in object.days:
                                if d == day_name:
                                    ClassesCounselor.append(OfferCode(offer_code = object.offer_code,days = object.days,
                                    start_time= object.start_time,end_time= object.end_time,room = object.room,
                                    subject_code = object.subject_code,sem_id=object.sem_id, academic_year = object.academic_year,))
                        ClassesCounselorCheck = bool(ClassesCounselor)    
                else:
                    ClassesCounselorCheck=False

                start = datetime.strptime('8:00:00', '%H:%M:%S').time()
                end = datetime.strptime('17:00:00', '%H:%M:%S').time()
                        
                

                TimeTaken=0
                TimeTaken1=0
                counter=0

                if (ClassesCounselorCheck==False and ScheduledReferralbyDayCheck ==False):
                        startTime =datetime.strptime('8:00:00', '%H:%M:%S').time()
                        endTime =datetime.strptime('9:00:00', '%H:%M:%S').time()
                        time1=startTime
                        time2=endTime
                        finder=1     
                elif(ClassesCounselorCheck==False and ScheduledReferralbyDayCheck ==True):
                            for x in range(len(timeArray)):
                                if(timeArray[x] >= start and timeArray[x] < end):
                                    for object2 in ScheduledReferralbyDay:
                                        if(timeArray[x+1]<=object2.end_time and timeArray[x]>=object2.start_time):
                                            TimeTaken+=1
                                            
                                    if(TimeTaken==0 and counter==0):
                                        time1=timeArray[x]
                                        counter=1
                                        TimeTaken=0;	
                                    elif(TimeTaken==0 and counter==1):
                                        time2=timeArray[x+1]
                                        counter=0
                                        finder=1
                                        break
                                    elif(TimeTaken!=0):
                                        time1=''
                                        TimeTaken=0

                elif(ClassesCounselorCheck==True and ScheduledReferralbyDayCheck ==False):
                        for x in range(len(timeArray)):
                                if(timeArray[x] >= start and timeArray[x] < end):
                                    for object2 in ClassesCounselor:
                                            if(timeArray[x+1]<=object2.end_time and timeArray[x]>=object2.start_time):
                                                TimeTaken+=1
                                    if(TimeTaken==0 and counter==0):
                                        time1=timeArray[x]
                                        counter=1
                                        TimeTaken=0;	
                                    elif(TimeTaken==0 and counter==1):
                                        time2=timeArray[x+1]
                                        counter=0
                                        TimeTaken=0
                                        finder=1
                                        break
                                    elif(TimeTaken!=0):
                                        time1=''
                                        TimeTaken=0
                elif(ClassesCounselorCheck==True and ScheduledReferralbyDayCheck ==True):
                        for x in range(len(timeArray)):
                            if(timeArray[x] >= start and timeArray[x] < end):
                                for object2 in ScheduledReferralbyDay:
                                    if(timeArray[x+1]<=object2.end_time and timeArray[x]>=object2.start_time):
                                        TimeTaken+=1
                                if(TimeTaken==0):
                                    for object3 in ClassesCounselor:
                                        if(timeArray[x+1]<=object3.end_time and timeArray[x]>=object3.start_time):
                                            TimeTaken1+=1
                                    if(TimeTaken1==0 and counter==0):
                                        time1=timeArray[x]
                                        counter=1
                                        TimeTaken=0	
                                        TimeTaken1=0
                                    elif (TimeTaken1==0 and counter==1):
                                        time2=timeArray[x+1]
                                        finder=1
                                        counter=0
                                        TimeTaken=0	
                                        TimeTaken1=0
                                        break
                                    elif(TimeTaken1!=0):
                                        time1=''
                                        TimeTaken=0
                                        TimeTaken1=0
                                        counter=0
                                            
                                else:
                                    counter=0
                                    TimeTaken=0
                                    time1=''
                            else:
                                counter=0
                                TimeTaken=0
                                time1='' 
                ScheduledReferralbyDay=[]
                ClassesCounselor=[]
            print("aaaa")
            print(time1)
            print(time2)
            print(tomorrow)
            if(time1!='' and time2!=''):
                schedForm.save()
                qs = Counselor.objects.get(program_designation = degree.program_code)
                sched = StudentSetSched(studnumber=student_name.studnumber,
                firstname=student_name.firstname,lastname=student_name.lastname,
                degree_program = degree.program_code,
                reasons=reasons,counselor=qs.employee_id, 
                start_time = time1 , end_time = time2, date = tomorrow )
                sched.save()
                schedForm = StudentSetSchedForm(instance=student_name)
                context = {"schedform": schedForm,"form": student_name}
                notif = notif + 1 
                notif1 = notif1 + 1
                create_notification(qs.employee_id, user, 'appointment', extra_id=int(student_name.studnumber), schedDay = tomorrow , schedStartTime = time1 , schedEndTime = time2)
                messages.info(request, 'Successfully Set Schedule')
                print("eeeeeeeee")

    context = {"schedform": schedForm,"form": student_name}
    return render(request, "student/schedule.html",context)

@login_required
def view_schedule_student(request, *args, **kwargs):
    user = request.session.get('username')
    today = date.today()
    now = datetime.now()
    day_name=now.strftime("%a")
    getsched = []
    classForToday = []
    getScheduleToday = StudentSetSched.objects.filter(date=today)
    getStudentsload = Studentsload.objects.filter(studnumber = user)  
    getOffercode = OfferCode.objects.all() 
    for sl in getStudentsload: 
        for oc in getOffercode: 
            if sl.offer_code_id == oc.offer_code:
                getsched.append(OfferCode(offer_code = oc.offer_code,days = oc.days,
                start_time= oc.start_time,end_time= oc.end_time,room = oc.room,
                subject_code = oc.subject_code,sem_id=oc.sem_id, academic_year = oc.academic_year))
    for sched in getsched:
        for d in sched.days:
            if d == day_name:
                classForToday.append(OfferCode(offer_code = sched.offer_code,days = sched.days,start_time= sched.start_time,end_time= sched.end_time,room = sched.room,
                subject_code = sched.subject_code,sem_id=sched.sem_id, academic_year = sched.academic_year))

    student_name = AllStudent.objects.filter(studnumber = user)
    # {"object":classForToday,"object_list":getScheduleToday,"form": student_name}
    return render(request, "student/viewschedule.html", {"object":classForToday,"object_list":getScheduleToday,"form": student_name})

@login_required
def view_class_students(request, offer_code, sem_id, year):
    user = request.session.get('username')
    student_name = AllStudent.objects.filter(studnumber = user)
    session = OfferCode.objects.get(offer_code=offer_code, sem_id=sem_id, academic_year=year)
    context = {"object":session,"form": student_name}
    return render(request, "student/viewclass.html", context)

@login_required
def view_appointment_students(request, id):
    user = request.session.get('username')
    student_name = AllStudent.objects.filter(studnumber = user)
    getStudentsSched = StudentSetSched.objects.get(id = id)  
    context = {"object":getStudentsSched,"form": student_name}
    return render(request, "student/viewappointment.html", context)


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
    if notif is not None:
        print("becca")
    student_name = AllStudent.objects.filter(studnumber = user)
    return render(request, 'student/notification.html', {"notifications":notif,"form": student_name})

@login_required
def student_notif_detail(request, id):
    global notif1
    detail = []
    student = TeachersReferral.objects.all()
    for referedStud in student:
        print(referedStud.id)
        if (referedStud.id == id):
            detail.append(TeachersReferral(firstname=referedStud.firstname, 
            lastname=referedStud.lastname,studnumber=referedStud.studnumber,
            degree_program = referedStud.degree_program,subject_referred=referedStud.subject_referred,
            reasons=referedStud.reasons,behavior_problem = referedStud.behavior_problem,date =referedStud.date, 
            start_time =referedStud.start_time, end_time =referedStud.end_time))
    if notif1 != 0:
        notif1 = notif1 - 1
    user = request.session.get('username')
    student_name = AllStudent.objects.filter(studnumber = user)
    return render(request, 'student/notif_detail.html', {"object_list":detail, "form": student_name})



#student














































# @login_required(login_url='login')
# def counselor_setSchedule(request, pk):
    # counselor = CounselorSchedule.objects.get(time1=pk)
    # form = CounselorScheduleForm(instance=counselor)
    # objectss= CounselorSchedule.objects.order_by('schedid')
    
    # if request.method == "POST":
    #     print("chuchu")
    #     form = CounselorScheduleForm(request.POST, instance=counselor)
    #     if form.is_valid():
    #         schedid = request.POST['schedid']
    #         service_offered = request.POST['service_offered']
    #         description= request.POST['description']
    #         CounselorSchedule.objects.filter(time1=pk).update(service_offered=service_offered,description=description)
    #         counselorsss = CounselorSchedule.objects.order_by('schedid')
    #         context = {"object" : counselorsss}
    #         return render(request, "counselor/schedule.html",context)
    # user = request.session.get('username')
    # counselor_name = Faculty.objects.filter(employee_id = user)
    # return render(request, "counselor/set_schedule.html",{"form": counselor_name})


# @login_required
# def manual_detail(request, pk, created_by, id):
#     global notif
#     user = request.session.get('username')
#     counselor_name = Faculty.objects.filter(employee_id = user)
#     student = TeachersReferral.objects.filter(studnumber=pk, employeeid=created_by, id=id)
#     if notif != 0 and notif > 0:
#         notif-=1
#     return render(request, 'counselor/manual_detail.html', {"object":student,"object_list": counselor_name})



# @login_required(login_url='login')
# def student_schedule(request, *args, **kwargs):
    # studentSchedulelist = []
    # user = request.session.get('username')
    # studentSubject = Studentsload.objects.filter(studnumber = user)
    # allSubject = SubjectOffered.objects.all()
    # studentssss = StudentSchedule.objects.order_by('schedid')
    # stud=StudentSchedule.objects.all()
    # for object in allSubject:
    #     for object1 in studentSubject:
    #         if object.offer_no == object1.offer_no:
    #             studentSchedulelist.append(SubjectOffered(object.offer_no, 
    #             object.subject_no,object.subject_title,object.dayofsub,
    #             object.start_time,object.end_time,object.units))
    # for object in studentSchedulelist:
    #     for object1 in stud:
    #         if(object.start_time==object1.time1 or object.end_time==object1.time2):
    #             StudentSchedule.objects.filter(schedid=object1.schedid).update(schedule='CLASS',description=object.offer_no)
    # context = {"object" : studentssss}
  
    # return render(request, "student/schedule.html", context )


# @login_required(login_url='login')
# def new(request,stud):
#     user = request.session.get('username')
#     allstud = AllStudent.objects.get(student_id=stud)
#     form = ReferralForm(instance=allstud)
#     name = ''
#     stdnum= ''
#     sub= ''
#     couns =''
#     global notif
#     global notif1
#     if request.method=="POST":
#        form = ReferralForm(request.POST, instance=allstud)
#        if form.is_valid():
#             form.save()
#             return render(request, "teacher/teacher_home.html")
#        firstname= request.POST['firstname']
#        name = firstname
#        lastname= request.POST['lastname']
#        studnumber= request.POST['studnumber']
#        stdnum= studnumber
#        degree_program= request.POST['degree_program']
#        subject_referred= request.POST['subject_referred']
#        sub = subject_referred
#        reasons= request.POST['reasons']
#        print("baaaaa")
#        qs = Counselor.objects.get(program_designation = degree_program)
#        couns = qs.employeeid
#        print("precious giffftt")
#        print(couns)
#        studentInfo = TeachersReferral(firstname=firstname, 
#        lastname=lastname,studnumber=studnumber,
#        degree_program = degree_program,subject_referred=subject_referred,
#        reasons=reasons,counselor=qs.employeeid,employeeid=user)
#        studentInfo.save()
#        notif = notif + 1
#        notif1 = notif1 + 1
#        create_notification(couns, user, 'manual_referral', extra_id=int(stdnum))
#     else:
#         TeachersReferralForm()
#     studentSched=StudentSchedule.objects.all()
#     counselorSched= CounselorSchedule.objects.all()
#     for index, objectstud in enumerate(studentSched):
#         if studentSched[index].schedule==None and studentSched[index+1].schedule==None:
#             for index, object in enumerate(counselorSched):
#                 if counselorSched[index].service_offered==None and counselorSched[index+1].service_offered==None:
#                     CounselorSchedule.objects.filter(schedid=counselorSched[index].schedid).update(
#                         service_offered='COUNSELING',description=name)
#                     CounselorSchedule.objects.filter(schedid=counselorSched[index+1].schedid).update(
#                         service_offered='COUNSELING',description=name)
#                     studentNumber= stdnum
#                     subject= sub
#                     teacher_referred= user
#                     print(studentNumber,subject,teacher_referred)
#                     getReferralNotDone= TeachersReferral.objects.filter(status = None, employeeid=user)
#                     for object1 in getReferralNotDone:
#                         if object1.studnumber==studentNumber and object1.subject_referred==subject and object1.employeeid==user:
#                             print(object1.id)
#                             TeachersReferral.objects.filter(id=object1.id).update(
#                                 start_time=counselorSched[index].time1,end_time=counselorSched[index+1].time2)
                            
#                     break
#     user_name = Faculty.objects.filter(employee_id = user)
#     return render(request, "teacher/new.html",{"form": user_name,"form1": form})




# CounselorSchedule
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



# @login_required(login_url='login')
# def export_studentslist(request):
#     students_resource = TeachersloadResource()
#     dataset = students_resource.export()
#     response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="students.xls"'
#     return response



#uploaddb
@login_required(login_url='login')
def uploaddb_home_view(request, *args, **kwargs):
    return render(request, "uploaddb/uploaddb_home.html", {})


@login_required(login_url='login')
def uploaddb_schooloffices(request):
    if request.method == 'POST':
        SchoolOfficesResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        for data in imported_data:
        	value = SchoolOffices(
                data[0],
                data[1], 
                data[2]
                )
        	value.save()     
    return render(request, "uploaddb/uploaddb_schooloffices.html")

@login_required(login_url='login')
def uploaddb_department(request):
    if request.method == 'POST':
        DepartmentResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        for data in imported_data:
        	value = Department(
                data[0],
                data[1], 
                data[2]
                )
        	value.save()     
    return render(request, "uploaddb/uploaddb_department.html")

@login_required(login_url='login')
def uploaddb_degreeprogram(request):
    if request.method == 'POST':
        DegreeProgramResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        for data in imported_data:
        	value = DegreeProgram(
                data[0],
                data[1], 
                data[2],
                data[3]
                )
        	value.save()     
    return render(request, "uploaddb/uploaddb_degreeprogram.html")


@login_required(login_url='login')
def uploaddb_allfaculty(request):
    if request.method == 'POST':
        AllFacultyResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        for data in imported_data:
        	value = AllFaculty(
                data[0],
                data[1], 
                data[2],
                data[3],
                data[4], 
                data[5],
                )
        	value.save()     
    return render(request, "uploaddb/uploaddb_allfaculty.html")

@login_required(login_url='login')
def uploaddb_allsubject(request):
    if request.method == 'POST':
        AllSubjectResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        for data in imported_data:
        	value = AllSubject(
                data[0],
                data[1], 
                data[2],
                data[3],
                )
        	value.save()     
    return render(request, "uploaddb/uploaddb_allsubject.html")

@login_required(login_url='login')
def uploaddb_semester(request):
    if request.method == 'POST':
        SemesterResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        for data in imported_data:
        	value = Semester(
                data[0],
                data[1], 
                )
        	value.save()     
    return render(request, "uploaddb/uploaddb_semester.html")

@login_required(login_url='login')
def uploaddb_offercode(request):
    if request.method == 'POST':
        OfferCodeResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        for data in imported_data:
        	value = OfferCode(
                data[0],
                data[1], 
                data[2],
                data[3],
                data[4], 
                data[5], 
                data[6], 
                data[7], 
                )
        	value.save()     
    return render(request, "uploaddb/uploaddb_offerCode.html")



@login_required(login_url='login')
def uploaddb_counselor(request):
    if request.method == 'POST':
        CounselorResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read(),format='xlsx')
        for data in imported_data:
        	value = Counselor(
                data[0],
                data[1], 
                data[2],
                data[3],
                )
        	value.save()     
    return render(request, "uploaddb/uploaddb_counselor.html")
#uploaddb

