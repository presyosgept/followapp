from multiselectfield import MultiSelectField
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class MyTable(models.Model):
    class Meta:
        unique_together = (('key1', 'key2', 'key3'))

    key1 = models.CharField(max_length=220)
    key2 = models.CharField(max_length=220)
    key3 = models.CharField(max_length=220)


class SchoolOffices(models.Model):
    school_id = models.CharField(max_length=15, primary_key=True)
    school_code = models.CharField(max_length=220)
    school_office_name = models.CharField(max_length=220)


class Department(models.Model):
    department_id = models.CharField(max_length=15, primary_key=True)
    department_name = models.CharField(max_length=220)
    school_id = models.ForeignKey(SchoolOffices, on_delete=models.CASCADE)


class DegreeProgram(models.Model):
    program_id = models.CharField(max_length=15, primary_key=True)
    program_code = models.CharField(max_length=220)
    program_name = models.CharField(max_length=220)
    school_id = models.ForeignKey(SchoolOffices, on_delete=models.CASCADE)


class AllStudent(models.Model):
    studnumber = models.CharField(max_length=15, primary_key=True)
    lastname = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    middlename = models.CharField(max_length=220)
    degree_program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE)
    year = models.IntegerField()
    student_email = models.EmailField(max_length=254)
    role = models.CharField(max_length=220, blank=True, null=True)


class StudentInfo(models.Model):
    studnumber = models.CharField(max_length=15, primary_key=True)
    lastname = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    middlename = models.CharField(max_length=220)
    degree_program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE)
    year = models.IntegerField()
    student_email = models.EmailField(max_length=254)
    student_contact_number = models.CharField(max_length=220)
    mother_lastname = models.CharField(max_length=220)
    mother_firstname = models.CharField(max_length=220)
    father_lastname = models.CharField(max_length=220)
    father_firstname = models.CharField(max_length=220)
    guardian_lastname = models.CharField(max_length=220, blank=True, null=True)
    guardian_firstname = models.CharField(
        max_length=220, blank=True, null=True)
    mother_contact_number = models.CharField(
        max_length=220, blank=True, null=True)
    father_contact_number = models.CharField(
        max_length=220, blank=True, null=True)
    guardian_contact_number = models.CharField(
        max_length=220, blank=True, null=True)
    status = models.CharField(max_length=254, default='undone')


class Faculty(models.Model):
    employee_id = models.CharField(max_length=15, primary_key=True)
    lastname = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=220)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)


class AccountCreated(models.Model):
    id_number = models.CharField(max_length=15, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=220, blank=True, null=True)


class AccountsApi(models.Model):
    id_number = models.CharField(max_length=15, primary_key=True)
    email = models.CharField(max_length=220)
    code = models.CharField(max_length=220, blank=True, null=True)


class OfferCode(models.Model):
    class Meta:
        unique_together = (('offer_code', 'sem_id', 'academic_year'))

    offer_code = models.CharField(max_length=225, primary_key=True)
    days = ArrayField(models.CharField(max_length=220), default=list)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=225, default=None)
    subject_code = models.CharField(max_length=225, default=None)
    sem_id = models.CharField(max_length=225, default=None)
    academic_year = models.CharField(max_length=225, default=None)
    choice = models.CharField(max_length=220, blank=True, null=True)


class Offering(models.Model):
    SEMESTER = (('1ST SEM', '1ST SEM'),
                ('2ND SEM', '2ND SEM'),
                ('SUMMER', 'SUMMER'))
    semester = models.CharField(
        max_length=220, choices=SEMESTER, default='1ST SEM', null=False, blank=False)
    SCHOOL_YEAR = (('2019-2020', '2019-2020'),
                   ('2020-2021', '2020-2021'),
                   ('2021-2022', '2021-2022'))
    school_year = models.CharField(
        max_length=220, choices=SCHOOL_YEAR, default='2021-2022',  null=False, blank=False)


class DepaChoice(models.Model):
    DEPA_CHOICE = (('Department of Language and Literature', 'Department of Language and Literature'),
                   ('Department of Social Sciences and Philosophy',
                    'Department of Social Sciences and Philosophy'),
                   ('Department of Mathematics and Sciences',
                    'Department of Mathematics and Sciences'),
                   ('Department of Journalism and Communication',
                    'Department of Journalism and Communication'),
                   ('Department of Psychology and Library Information Science',
                    'Department of Psychology and Library Information Science'),
                   ('Department of Accountancy and Finance',
                    'Department of Accountancy and Finance'),
                   ('Department of Business and Entrepreneurship',
                    'Department of Business and Entrepreneurship'),
                   ('Department of Marketing and Human Resource Management',
                    'Department of Marketing and Human Resource Management'),
                   ('Department of Computer Science and Information Technology',
                    'Department of Computer Science and Information Technology'),
                   ('Student Development and Placement Center',
                    'Student Development and Placement Center'),
                   ('Center for Religious Education',
                    'Center for Religious Education'),
                   ('Safety and Security Department',
                    'Safety and Security Department'),
                   ('Department of Education', 'Department of Education'))
    depa_choice = models.CharField(max_length=220, choices=DEPA_CHOICE,
                                   default='Department of Language and Literature', null=False, blank=False)


class AllSubject(models.Model):
    subject_code = models.CharField(max_length=225, primary_key=True)
    subject_title = models.CharField(max_length=220)
    units = models.CharField(max_length=220)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)


class Semester(models.Model):
    sem_id = models.CharField(max_length=225, primary_key=True)
    semester = models.CharField(max_length=225)


class SubjectWithSem(models.Model):
    id = models.CharField(max_length=225, primary_key=True)
    offer_code = models.CharField(max_length=225)
    sem_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_code = models.ForeignKey(AllSubject, on_delete=models.CASCADE)


class Facultyload(models.Model):
    id = models.CharField(max_length=220, primary_key=True)
    offer_code = models.ForeignKey(
        OfferCode, on_delete=models.CASCADE, null=True)
    employee_id = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True)


class Studentsload(models.Model):
    id = models.CharField(max_length=220, primary_key=True)
    offer_code = models.ForeignKey(
        OfferCode, on_delete=models.CASCADE, null=True)
    studnumber = models.ForeignKey(
        AllStudent, on_delete=models.CASCADE, null=True)


class TeachersReferral(models.Model):
    studnumber = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    lastname = models.CharField(max_length=220)
    degree_program = models.CharField(max_length=220)
    subject_referred = models.CharField(max_length=220)
    reasons = models.CharField(max_length=10000)
    counselor = models.CharField(max_length=220)
    employeeid = models.CharField(max_length=220, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    status = models.CharField(
        max_length=220, blank=True, null=True, default='pending')
    BEHAVIOR_PROBLEM = (('CHEATING', 'CHEATING'),
                        ('TARDINESS', 'TARDINESS'), ('DISRESPECTFUL', 'DISRESPECTFUL'),
                        ('ATTITUDE', 'ATTITUDE'), ('USING GADGETS IN CLASS',
                                                   'USING GADGETS IN CLASS'),
                        ('GRUBBING', 'GRUBBING'), ('OTHERS', 'OTHERS'))
    behavior_problem = MultiSelectField(
        max_length=220, choices=BEHAVIOR_PROBLEM, null=True, blank=True)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    choice = models.CharField(max_length=220, blank=True, null=True)


class StudentSetSched(models.Model):
    studnumber = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    lastname = models.CharField(max_length=220)
    degree_program = models.CharField(max_length=220)
    reasons = models.CharField(max_length=10000)
    counselor = models.CharField(max_length=220)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)


class CounselorFeedback(models.Model):
    feedback = models.CharField(max_length=10000, null=True, blank=True)
    remarks = models.CharField(max_length=10000, null=True, blank=True)


class SubjectOffered(models.Model):
    offer_no = models.CharField(max_length=220, primary_key=True)
    subject_no = models.CharField(max_length=220)
    subject_title = models.CharField(max_length=220)
    dayofsub = ArrayField(models.CharField(
        max_length=220), default=list, blank=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    units = models.CharField(max_length=220)


class Counselor(models.Model):
    PROGRAM_DESIGNATION = (('BSIT', 'BSIT'),
                           ('BSIS', 'BSIS'), ('BSCS', 'BSCS'),
                           ('BSA', 'BSA'))
    program_designation = MultiSelectField(
        max_length=220, choices=PROGRAM_DESIGNATION, null=True, blank=True)
    employee_id = models.CharField(max_length=220, primary_key=True)
    firstname = models.CharField(max_length=220)
    lastname = models.CharField(max_length=220)


class Notification(models.Model):
    AUTOMATIC_REFERRAL = 'automatic_referral'
    MANUAL_REFERRAL = 'manual_referral'
    APPOINTMENT = 'appointment'

    CHOICES = (
        (AUTOMATIC_REFERRAL, 'automatic_referral'),
        (MANUAL_REFERRAL, 'manual_referral'),
        (APPOINTMENT, 'appointment')
    )

    to_user = models.CharField(max_length=220, null=True, blank=True)
    notification_type = models.CharField(max_length=100, choices=CHOICES)
    is_read_student = models.BooleanField(default=False)
    is_read_counselor = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=220, null=True, blank=True)
    schedDay = models.DateTimeField(blank=True, null=True)
    schedStartTime = models.TimeField(blank=True, null=True)
    schedEndTime = models.TimeField(blank=True, null=True)


class NotificationFeedback(models.Model):
    FEEDBACK_TEACHER = 'feedback_teacher'
    FEEDBACK_STUDENT = 'feedback_student'

    CHOICES = (
        (FEEDBACK_TEACHER, 'feedback_teacher'),
        (FEEDBACK_STUDENT, 'feedback_student')
    )

    to_user = models.CharField(max_length=220, null=True, blank=True)
    notification_type = models.CharField(max_length=100, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)
    referral_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=220, null=True, blank=True)
