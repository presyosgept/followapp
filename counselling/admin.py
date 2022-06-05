from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import StudentInfo, FilterDate, AccountsApi, Facultyload, Faculty, NotificationFeedback, Notification, TeachersReferral, SubjectOffered, Studentsload, Counselor, Calendar
from .models import NewTime, SetScheduleCounselor, NewDepartment, Offering, StudentSetSched, CounselorFeedback, SubjectWithSem, Semester, Subject, OfferCode, AccountCreated, SchoolOffices, DegreeProgram, AllStudent

admin.site.register(NewTime)
admin.site.register(SetScheduleCounselor)
admin.site.register(StudentInfo)
admin.site.register(StudentSetSched)
admin.site.register(Offering)
admin.site.register(Calendar) 
admin.site.register(FilterDate)
admin.site.register(NewDepartment)


admin.site.register(CounselorFeedback)


class CounselorFeedbackAdmin(ImportExportModelAdmin):
    list_display = ('feedback', 'remarks')


admin.site.register(Facultyload)


class FacultyloadAdmin(ImportExportModelAdmin):
    list_display = ('id', 'offer_code', 'employee_id')


admin.site.register(SubjectWithSem)


class SubjectWithSemAdmin(ImportExportModelAdmin):
    list_display = ('id', 'offer_code', 'sem_id', 'subject_code')


admin.site.register(Semester)


class SemesterAdmin(ImportExportModelAdmin):
    list_display = ('sem_id', 'semester')


admin.site.register(OfferCode)


class OfferCodeAdmin(ImportExportModelAdmin):
    list_display = ('offer_code', 'days', 'start_time', 'end_time', 'room',
                    'subject_code', 'sem_id', 'academic_year')


admin.site.register(SchoolOffices)


class SchoolOfficesAdmin(ImportExportModelAdmin):
    list_display = ('school_code', 'school_office_name')


admin.site.register(DegreeProgram)


class DegreeProgramAdmin(ImportExportModelAdmin):
    list_display = ('program_id', 'program_code',
                    'program_name', 'school_code')


admin.site.register(AllStudent)


class AllStudentAdmin(ImportExportModelAdmin):
    list_display = ('studnumber', 'lastname', 'firstname', 'middlename',
                    'degree_program', 'year', 'email', 'role')


# iupload

admin.site.register(Faculty)


class FacultyAdmin(ImportExportModelAdmin):
    list_display = ('employee_id', 'lastname', 'firstname',
                    'email', 'role', 'department_id')


admin.site.register(AccountCreated)


class AccountCreatedAdmin(ImportExportModelAdmin):
    list_display = ('id_number', 'email', 'password')


admin.site.register(AccountsApi)


class AccountsApiAdmin(ImportExportModelAdmin):
    list_display = ('id_number', 'email', 'code')


admin.site.register(TeachersReferral)


class TeachersReferralAdmin(ImportExportModelAdmin):
    list_display = ('studnumber', 'firstname', 'lastname', 'degree_program', 'subject_referred', 'reasons',
                    'counselor', 'employeeid', 'start_time', 'end_time', 'date', 'status', 'behavior_problem', 'feedback')


admin.site.register(SubjectOffered)


class SubjectOfferedAdmin(ImportExportModelAdmin):
    list_display = ('offer_no', 'subject_no', 'subject_title',
                    'dayofsub', 'start_time', 'end_time', 'units')


admin.site.register(Studentsload)


class Studentsload(ImportExportModelAdmin):
    list_display = ('id', 'offer_code', 'studnumber')


admin.site.register(Counselor)


class CounselorAdmin(ImportExportModelAdmin):
    list_display = ('employee_id', 'firstname',
                    'lastname', 'school_choice', 'program_designation')


admin.site.register(Notification)
admin.site.register(NotificationFeedback)
