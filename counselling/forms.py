from .models import Counselor, CounselorSchedule, StudentSchedule
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

from django import forms

class TeachersReferralForm(forms.Form):
    studnumber = forms.CharField()
    firstname = forms.CharField()
    lastname =  forms.CharField()
    degree_program = forms.CharField()
    subject_referred =  forms.CharField()
    reasons = forms.CharField(widget=forms.Textarea)

class StudentsForm(forms.Form):
    studnumber = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.CharField()
    course = forms.CharField()
    year = forms.CharField()
    role = forms.CharField()

class TeachersloadForm(forms.Form):
    employeeid = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    external_email = forms.CharField()
    role = forms.CharField()

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class SubjectOfferedForm(forms.Form):
    offer_no = forms.CharField()
    subject_no = forms.CharField()
    subject_title = forms.CharField()
    dayofsub = forms.CharField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    units = forms.CharField()
    
class FacultyloadForm(forms.Form):
    offer_no = forms.CharField()
    employeeid = forms.CharField()
 
class StudentsloadForm(forms.Form):
    id = forms.CharField()
    offer_no = forms.CharField()
    studnumber = forms.CharField()

# class CounselorForm(forms.Form):
#     employeeid = forms.CharField()
#     firstname = forms.CharField()
#     lastname = forms.CharField()
#     program_designation = forms.CharField()
# class CounselorForm(forms.ModelForm):
# 	class Meta:
# 		model = Counselor
# 		fields = ['employeeid', 'firstname',  'lastname', 'program_designation']
class CounselorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CounselorForm, self).__init__(*args, **kwargs)
        self.fields['employeeid'].disabled = True
        self.fields['firstname'].disabled = True
        self.fields['lastname'].disabled = True

    class Meta:
        model = Counselor
        fields = ['employeeid', 'firstname', 'lastname', 'program_designation']
    
		
       


class CounselorScheduleForm(ModelForm):
    class Meta:
	    model = CounselorSchedule
	    fields = ['schedid','time1','time2', 'service_offered', 'description']

class StudentScheduleForm(ModelForm):
    class Meta:
	    model = StudentSchedule
	    fields = ['schedid','time1','time2', 'schedule', 'description']

from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput


