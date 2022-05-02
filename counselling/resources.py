from import_export import resources
from .models import Semester, Faculty, TeachersReferral, Counselor, SubjectOffered, Facultyload, Studentsload
from .models import NewTime, NewDepartment, SubjectWithSem, Subject, OfferCode, SchoolOffices, DegreeProgram, AllStudent

class TimeResource(resources.ModelResource):
    class Meta:
        model = NewTime
class NewDepartmentResource(resources.ModelResource):
    class Meta:
        model = NewDepartment


class SubjectWithSemResource(resources.ModelResource):
    class Meta:
        model = SubjectWithSem


class SemesterResource(resources.ModelResource):
    class Meta:
        model = Semester


class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subject


class OfferCodeResource(resources.ModelResource):
    class Meta:
        model = OfferCode


class SchoolOfficesResource(resources.ModelResource):
    class Meta:
        model = SchoolOffices

class DegreeProgramResource(resources.ModelResource):
    class Meta:
        model = DegreeProgram


class AllStudentResource(resources.ModelResource):
    class Meta:
        model = AllStudent


class FacultyResource(resources.ModelResource):
    class Meta:
        model = Faculty


class TeachersReferralResource(resources.ModelResource):
    class Meta:
        model = TeachersReferral


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
