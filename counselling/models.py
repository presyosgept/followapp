from multiselectfield import MultiSelectField
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class SchoolOffices(models.Model):
    #school_id = models.CharField(max_length=15, primary_key=True)
    school_code = models.CharField(max_length=220, primary_key=True)
    school_office_name = models.CharField(max_length=220)
    class Meta:
        verbose_name_plural = "SchoolOffices"


class NewDepartment(models.Model):
    department_id = models.CharField(max_length=15, primary_key=True)
    department_name = models.CharField(max_length=220)
    school_code = models.ForeignKey(SchoolOffices, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "NewDepartment"


class DegreeProgram(models.Model):
    program_id = models.CharField(max_length=15, primary_key=True)
    program_code = models.CharField(max_length=220)
    program_name = models.CharField(max_length=220)
    school_code = models.ForeignKey(SchoolOffices, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "DegreeProgram"


class AllStudent(models.Model):
    studnumber = models.CharField(max_length=15, primary_key=True)
    lastname = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    middlename = models.CharField(max_length=220)
    degree_program = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE)
    year = models.IntegerField()
    student_email = models.EmailField(max_length=254)
    role = models.CharField(max_length=220, blank=True, null=True)
    class Meta:
        verbose_name_plural = "AllStudent"


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
    class Meta:
        verbose_name_plural = "StudentInfo"


class Faculty(models.Model):
    employee_id = models.CharField(max_length=15, primary_key=True)
    lastname = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=220)
    department_id = models.ForeignKey(NewDepartment, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Faculty"


class AccountCreated(models.Model):
    id_number = models.CharField(max_length=15, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=220, blank=True, null=True)
    class Meta:
        verbose_name_plural = "AccountCreated"


class AccountsApi(models.Model):
    id_number = models.CharField(max_length=15, primary_key=True)
    email = models.CharField(max_length=220)
    code = models.CharField(max_length=220, blank=True, null=True)
    class Meta:
        verbose_name_plural = "AccountsApi"


class OfferCode(models.Model):
    class Meta:
        unique_together = (('offer_code', 'sem_id', 'academic_year'))
        verbose_name_plural = "Offering"

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
    qs = NewDepartment.objects.all()
    qs_code = []
    for obj in qs:
        qs_code.append([obj.department_name, obj.department_name])
    print('qs_code', qs_code)
    depa_choice = models.CharField(default='---',
                                   max_length=220, choices=qs_code, null=False, blank=False)
    class Meta:
        verbose_name_plural = "Offering"


class Subject(models.Model):
    subject_code = models.CharField(max_length=225, primary_key=True)
    subject_title = models.CharField(max_length=220)
    units = models.CharField(max_length=220)
    department_id = models.ForeignKey(NewDepartment, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Subject"


class Semester(models.Model):
    sem_id = models.CharField(max_length=225, primary_key=True)
    semester = models.CharField(max_length=225)
    class Meta:
        verbose_name_plural = "Semester"


class SubjectWithSem(models.Model):
    id = models.CharField(max_length=225, primary_key=True)
    offer_code = models.CharField(max_length=225)
    sem_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_code = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "SubjectWithSem"


class Facultyload(models.Model):
    id = models.CharField(max_length=220, primary_key=True)
    offer_code = models.ForeignKey(
        OfferCode, on_delete=models.CASCADE, null=True)
    employee_id = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "Facultyload"


class Studentsload(models.Model):
    id = models.CharField(max_length=220, primary_key=True)
    offer_code = models.ForeignKey(
        OfferCode, on_delete=models.CASCADE, null=True)
    studnumber = models.ForeignKey(
        AllStudent, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "Studentsload"


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
                        ('BAD ATTITUDE', 'BAD ATTITUDE'), ('OTHERS', 'OTHERS'))
    behavior_problem = MultiSelectField(
        max_length=220, choices=BEHAVIOR_PROBLEM, null=True, blank=True)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    choice = models.CharField(max_length=220, blank=True, null=True)
    class Meta:
        verbose_name_plural = "TeachersReferral"


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
    class Meta:
        verbose_name_plural = "StudentSetSched"


class CounselorFeedback(models.Model):
    feedback = models.CharField(max_length=10000, null=True, blank=True)
    remarks = models.CharField(max_length=10000, null=True, blank=True)
    class Meta:
        verbose_name_plural = "CounselorFeedback"


class SubjectOffered(models.Model):
    offer_no = models.CharField(max_length=220, primary_key=True)
    subject_no = models.CharField(max_length=220)
    subject_title = models.CharField(max_length=220)
    dayofsub = ArrayField(models.CharField(
        max_length=220), default=list, blank=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    units = models.CharField(max_length=220)
    class Meta:
        verbose_name_plural = "SubjectOffered"


class Counselor(models.Model):
    employee_id = models.CharField(max_length=220, primary_key=True)
    firstname = models.CharField(max_length=220)
    lastname = models.CharField(max_length=220)
    qs = DegreeProgram.objects.all()
    qs_code = []
    for obj in qs:
        qs_code.append(
            [obj.program_code, obj.program_code+' - '+obj.program_name])
    program_designation = MultiSelectField(
        max_length=220, choices=qs_code, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Counselor"


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
    class Meta:
        verbose_name_plural = "Notification"


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
    class Meta:
        verbose_name_plural = "NotificationFeedback"


class Calendar(models.Model):
    pickedDate = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Calendar"


class FilterDate(models.Model):
    pickedStartDate = models.DateField(null=True)
    pickedEndDate = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "FilterDate"


class SetScheduleCounselor(models.Model):
    employee_id = models.CharField(max_length=220, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    choice = models.CharField(max_length=220, blank=True, null=True)

    class Meta:
        verbose_name_plural = "SetScheduleCounselor"


class NewTime(models.Model):
    time_id = models.CharField(max_length=220, primary_key=True)
    time1 = models.TimeField()
    time2 = models.TimeField()

    class Meta:
        verbose_name_plural = "NewTime"
