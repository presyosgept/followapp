from .models import Counselor, CounselorFeedback,AccountCreated,TeachersReferral,AllStudent,StudentSetSched,Offering,DepaChoice
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from django import forms

class DepaChoiceForm(forms.ModelForm):
	class Meta:
		model = DepaChoice
		fields = '__all__'

class OfferingForm(forms.ModelForm):
	class Meta:
		model = Offering
		fields = '__all__'

class CounselorFeedbackForm(forms.ModelForm):
    feedback = forms.CharField(widget=forms.Textarea)
    remarks = forms.CharField(widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(CounselorFeedbackForm, self).__init__(*args, **kwargs)
    class Meta:
        model = CounselorFeedback
        fields = '__all__'
# # class FeedbackForm(forms.Form):
# #     feedback = forms.CharField(widget=forms.Textarea)

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

class AccountsForm(forms.Form):
    password = forms.CharField()

class VerificationForm(forms.Form):
    code = forms.CharField()

class AccountCreatedForm(forms.Form):
    id_number = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

class StudentSetSchedForm(forms.ModelForm):
    reasons = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(StudentSetSchedForm, self).__init__(*args, **kwargs)
        self.fields['studnumber'].disabled = True
        self.fields['firstname'].disabled = True
        self.fields['lastname'].disabled = True
    class Meta:
        model = StudentSetSched
        fields = ['studnumber', 'firstname', 'lastname',  'reasons']

class TeachersReferralForm(forms.ModelForm):
    reasons = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(TeachersReferralForm, self).__init__(*args, **kwargs)
        self.fields['studnumber'].disabled = True
        self.fields['firstname'].disabled = True
        self.fields['lastname'].disabled = True
        self.fields['subject_referred'].disabled = True
    class Meta:
        model = TeachersReferral
        fields = ['studnumber', 'firstname', 'lastname', 'behavior_problem','subject_referred','reasons','feedback']

class StudentsForm(forms.Form):
    studnumber = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.CharField()
    course = forms.CharField()
    year = forms.CharField()
    role = forms.CharField()


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


class CounselorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CounselorForm, self).__init__(*args, **kwargs)
        self.fields['employee_id'].disabled = True
        self.fields['firstname'].disabled = True
        self.fields['lastname'].disabled = True

    class Meta:
        model = Counselor
        fields = ['employee_id', 'firstname', 'lastname', 'program_designation']
    
		
       


# class CounselorScheduleForm(ModelForm):
#     class Meta:
# 	    model = CounselorSchedule
# 	    fields = ['schedid','time1','time2', 'service_offered', 'description']




