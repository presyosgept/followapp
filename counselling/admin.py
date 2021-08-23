from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Notification,CounselorSchedule,TeachersReferral, Students, Teachersload, SubjectOffered, Facultyload, Studentsload, Counselor, StudentSchedule

admin.site.register(TeachersReferral)
class TeachersReferralAdmin(ImportExportModelAdmin):
    list_display = ('studnumber','firstname', 'lastname','degree_program','subject_referred', 'reasons','counselor','employeeid','start_time','end_time','date','status')

admin.site.register(Students)
class StudentsAdmin(ImportExportModelAdmin):
    list_display = ('studnumber','firstname', 'lastname','email','course','yeary','role')

admin.site.register(Teachersload)
class TeachersloadAdmin(ImportExportModelAdmin):
    list_display = ('employeeid','firstname', 'lastname','external_email','role')

admin.site.register(SubjectOffered)
class SubjectOfferedAdmin(ImportExportModelAdmin):
    list_display = ('offer_no','subject_no', 'subject_title','dayofsub','start_time','end_time','units')
    
admin.site.register(Facultyload)
class FacultyloadAdmin(ImportExportModelAdmin):
    list_display = ('offer_no','employeeid')
   
admin.site.register(Studentsload)
class StudentsloadAdmin(ImportExportModelAdmin):
    list_display = ('id','offer_no','studnumber')

admin.site.register(Counselor)
class CounselorAdmin(ImportExportModelAdmin):
    list_display = ('employeeid', 'firstname', 'lastname','program_designation')

admin.site.register(CounselorSchedule)
class CounselorScheduleAdmin(ImportExportModelAdmin):
    list_display = ('schedid','time1','time2', 'service_offered','description')

admin.site.register(StudentSchedule)
class StudentScheduleAdmin(ImportExportModelAdmin):
    list_display = ('schedid','time1','time2', 'schedule','description')

admin.site.register(Notification) 
