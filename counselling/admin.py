from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import StudentInfo, AccountsApi, Facultyload, Faculty, NotificationFeedback, Notification, TeachersReferral, SubjectOffered, Studentsload, Counselor
from .models import DepaChoice, Offering, StudentSetSched, CounselorFeedback, MyTable, SubjectWithSem, Semester, AllSubject, OfferCode, AccountCreated, SchoolOffices, Department, DegreeProgram, AllStudent

admin.site.register(StudentInfo)
admin.site.register(StudentSetSched)
admin.site.register(Offering)
admin.site.register(DepaChoice)

admin.site.register(CounselorFeedback)


class CounselorFeedbackAdmin(ImportExportModelAdmin):
    list_display = ('feedback', 'remarks')


admin.site.register(MyTable)


class MyTableAdmin(ImportExportModelAdmin):
    list_display = ('key1', 'key2', 'key3')


admin.site.register(Facultyload)


class FacultyloadAdmin(ImportExportModelAdmin):
    list_display = ('id', 'offer_code', 'employee_id')


admin.site.register(SubjectWithSem)


class SubjectWithSemAdmin(ImportExportModelAdmin):
    list_display = ('id', 'offer_code', 'sem_id', 'subject_code')


admin.site.register(Semester)


class SemesterAdmin(ImportExportModelAdmin):
    list_display = ('sem_id', 'semester')


admin.site.register(AllSubject)


class AllSubjectAdmin(ImportExportModelAdmin):
    list_display = ('subject_code', 'subject_title', 'units', 'department_id')


admin.site.register(OfferCode)


class OfferCodeAdmin(ImportExportModelAdmin):
    list_display = ('offer_code', 'days', 'start_time', 'end_time', 'room',
                    'subject_code', 'sem_id', 'academic_year')


admin.site.register(SchoolOffices)


class SchoolOfficesAdmin(ImportExportModelAdmin):
    list_display = ('school_id', 'school_code', 'school_office_name')


admin.site.register(Department)


class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ('department_id', 'department_name', 'school_id')


admin.site.register(DegreeProgram)


class DegreeProgramAdmin(ImportExportModelAdmin):
    list_display = ('program_id', 'program_code', 'program_name', 'school_id')


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
                    'lastname', 'program_designation')


admin.site.register(Notification)
admin.site.register(NotificationFeedback)
