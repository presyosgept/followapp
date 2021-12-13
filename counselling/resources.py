from import_export import resources
from .models import Semester, Faculty, TeachersReferral, Counselor, SubjectOffered, Facultyload, Studentsload
from .models import SubjectWithSem, AllSubject, OfferCode, SchoolOffices, Department, DegreeProgram, AllStudent


class SubjectWithSemResource(resources.ModelResource):
    class Meta:
        model = SubjectWithSem


class SemesterResource(resources.ModelResource):
    class Meta:
        model = Semester


class AllSubjectResource(resources.ModelResource):
    class Meta:
        model = AllSubject


class OfferCodeResource(resources.ModelResource):
    class Meta:
        model = OfferCode


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
