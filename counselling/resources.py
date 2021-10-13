from import_export import resources
from .models import Semester,Faculty,TeachersReferral, Counselor, SubjectOffered,NewFacultyload,Studentsload
from .models import OfferCode,AllSubjects,NewOfferCode,SchoolOffices,Department,DegreeProgram,AllStudent,AllFaculty

class SemesterResource(resources.ModelResource):
    class Meta:
        model = Semester

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

class AllStudentResource(resources.ModelResource):
    class Meta:
        model = AllStudent

class AllFacultyResource(resources.ModelResource):
    class Meta:
        model = AllFaculty

#iupload

class FacultyResource(resources.ModelResource):
    class Meta:
        model = Faculty



class TeachersReferralResource(resources.ModelResource):
    class Meta:
        model = TeachersReferral



class SubjectOfferedResource(resources.ModelResource):
    class Meta:
        model = SubjectOffered

class NewFacultyloadResource(resources.ModelResource):
    class Meta:
        model = NewFacultyload

class StudentsloadResource(resources.ModelResource):
    class Meta:
        model = Studentsload

class CounselorResource(resources.ModelResource):
    class Meta:
        model = Counselor    




