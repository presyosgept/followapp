from import_export import resources
from .models import StudentSchedule,CounselorSchedule,TeachersReferral, Counselor, Students, Teachersload,SubjectOffered,Facultyload,Studentsload

class TeachersReferralResource(resources.ModelResource):
    class Meta:
        model = TeachersReferral

class StudentsResource(resources.ModelResource):
    class Meta:
        model = Students

class TeachersloadResource(resources.ModelResource):
    class Meta:
        model = Teachersload

class SubjectOfferedResource(resources.ModelResource):
    class Meta:
        model = SubjectOffered

class FacultyloadResource(resources.ModelResource):
    class Meta:
        model = Facultyload

class StudentsloadResource(resources.ModelResource):
    class Meta:
        model = Studentsload

class CounselorResource(resources.ModelResource):
    class Meta:
        model = Counselor    

class CounselorScheduleResource(resources.ModelResource):
    class Meta:
        model = CounselorSchedule

class StudentScheduleResource(resources.ModelResource):
    class Meta:
        model = StudentSchedule


