from import_export import resources
from .models import Faculty,Student,CounselorSchedule,TeachersReferral, Counselor, Teachersload,SubjectOffered,NewFacultyload,NewStudentsload
from .models import OfferCode,AllSubjects,NewOfferCode,SchoolOffices,Department,DegreeProgram,AllStudents,AllFaculty

class OfferCodeResource(resources.ModelResource):
    class Meta:
        model = OfferCode

class AllSubjectsResource(resources.ModelResource):
    class Meta:
        model = AllSubjects

class NewOfferCodeResource(resources.ModelResource):
    class Meta:
        model = NewOfferCode

class SchoolOfficesResource(resources.ModelResource):
    class Meta:
        model = SchoolOffices

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department

class DegreeProgramResource(resources.ModelResource):
    class Meta:
        model = DegreeProgram

class AllStudentsResource(resources.ModelResource):
    class Meta:
        model = AllStudents

class AllFacultyResource(resources.ModelResource):
    class Meta:
        model = AllFaculty

#iupload
class StudentResource(resources.ModelResource):
    class Meta:
        model = Student

class FacultyResource(resources.ModelResource):
    class Meta:
        model = Faculty



class TeachersReferralResource(resources.ModelResource):
    class Meta:
        model = TeachersReferral

class TeachersloadResource(resources.ModelResource):
    class Meta:
        model = Teachersload

class SubjectOfferedResource(resources.ModelResource):
    class Meta:
        model = SubjectOffered

class NewFacultyloadResource(resources.ModelResource):
    class Meta:
        model = NewFacultyload

class NewStudentsloadResource(resources.ModelResource):
    class Meta:
        model = NewStudentsload

class CounselorResource(resources.ModelResource):
    class Meta:
        model = Counselor    

class CounselorScheduleResource(resources.ModelResource):
    class Meta:
        model = CounselorSchedule


