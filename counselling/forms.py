from multiselectfield import MultiSelectFormField
from django.forms.widgets import CheckboxSelectMultiple
from .models import Department, SchoolOffices, Calendar, StudentInfo, Counselor, CounselorFeedback, AccountCreated, TeachersReferral, AllStudent, StudentSetSched, Offering, DepaChoice
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from django import forms


from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class StudentInfoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentInfoForm, self).__init__(*args, **kwargs)
        self.fields['studnumber'].disabled = True
        self.fields['firstname'].disabled = True
        self.fields['lastname'].disabled = True
        self.fields['degree_program'].disabled = True
        self.fields['year'].disabled = True
        self.fields['student_email'].disabled = True

    class Meta:
        model = StudentInfo
        fields = ['studnumber', 'firstname', 'lastname',  'degree_program',
                  'year', 'student_email', 'student_contact_number',
                  'mother_lastname', 'mother_firstname',
                  'father_lastname', 'father_firstname',
                  'guardian_lastname', 'guardian_firstname',
                  'mother_contact_number',
                  'father_contact_number',
                  'guardian_contact_number',
                  ]


class DateForm(forms.Form):
    start_date = forms.DateField(widget=DateInput())
    end_date = forms.DateField(widget=DateInput())


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

    behavior_problem = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                                 choices=TeachersReferral.BEHAVIOR_PROBLEM)

    class Meta:
        model = TeachersReferral
        fields = ['studnumber', 'firstname', 'lastname',
                  'behavior_problem', 'subject_referred', 'reasons', 'feedback']


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


class ProgramForm(forms.Form):
    program = forms.CharField()


class DeleteSchoolOfficeForm(forms.Form):
    schoolform_code = forms.CharField()


class AddSchoolOfficeForm(forms.Form):
    school_code = forms.CharField()
    school_office_name = forms.CharField()

# class AddSchoolOfficeForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(AddSchoolOfficeForm, self).__init__(*args, **kwargs)
#         self.fields['school_id'].disabled = True

#     class Meta:
#         model = SchoolOffices
#         fields = ['school_id', 'school_code',
#                   'school_office_name']


class DeleteDepartmentForm(forms.Form):
    del_department_name_form = forms.CharField()


class AddDepartmentForm(forms.Form):
    department_name_form = forms.CharField()
    # school_code_form = forms.CharField()
    # def __init__(self, *args, **kwargs):
    #     super(AddDepartmentForm, self).__init__(*args, **kwargs)
    #     self.fields['school_code'].disabled = True

    # class Meta:
    #     model = Department
    #     fields = ['department_id', 'department_name',
    #               'school_code']


class CounselorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CounselorForm, self).__init__(*args, **kwargs)
        self.fields['employee_id'].disabled = True
        self.fields['firstname'].disabled = True
        self.fields['lastname'].disabled = True

    program_designation = MultiSelectFormField(widget=forms.CheckboxSelectMultiple,
                                               choices=Counselor.PROGRAM_DESIGNATION)

    class Meta:
        model = Counselor
        fields = ['employee_id', 'firstname',
                  'lastname', 'program_designation']


# class DateForm(forms.Form):
#     date = forms.DateTimeField(
#         input_formats=['%m/%d/%Y %H:%M'],
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )
class DateInput(forms.DateInput):
    input_type = 'date'


class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = '__all__'

        widgets = {
            'pickedDate': DateInput(format='%m/%d/%Y'),
        }


# class CounselorScheduleForm(ModelForm):
#     class Meta:
# 	    model = CounselorSchedule
# 	    fields = ['schedid','time1','time2', 'service_offered', 'description']
