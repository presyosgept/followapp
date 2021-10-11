from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class MyTable(models.Model):
    class Meta:
        unique_together = (('key1', 'key2','key3'))

    key1 = models.CharField(max_length=220)
    key2 = models.CharField(max_length=220)
    key3 = models.CharField(max_length=220)

class SchoolOffices(models.Model):
    school_id = models.CharField(max_length=15,primary_key=True)
    school_code = models.CharField(max_length=220)
    school_office_name = models.CharField(max_length=220)

class Department(models.Model):
    department_id = models.CharField(max_length=15,primary_key=True)
    department_name = models.CharField(max_length=220)
    school_id = models.ForeignKey(SchoolOffices,on_delete=models.CASCADE)

class DegreeProgram(models.Model):
    program_id = models.CharField(max_length=15,primary_key=True)
    program_code = models.CharField(max_length=220)
    program_name = models.CharField(max_length=220)
    school_id = models.ForeignKey(SchoolOffices,on_delete=models.CASCADE)

class AllStudents(models.Model):
    studnumber = models.CharField(max_length=15,primary_key=True)
    lastname = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    middlename = models.CharField(max_length=220)
    degree_program = models.ForeignKey(DegreeProgram,on_delete=models.CASCADE)
    year = models.IntegerField()
    email =  models.EmailField(max_length=254)

class Student(models.Model):
    studnumber = models.CharField(max_length=15,primary_key=True)
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=220)

class AllFaculty(models.Model):
    employee_id = models.CharField(max_length=15,primary_key=True)
    lastname = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    middlename = models.CharField(max_length=220)
    email = models.EmailField(max_length=254)
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)

class Faculty(models.Model):
    employee_id = models.CharField(max_length=15,primary_key=True)
    lastname = models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=220)


class AccountCreated(models.Model):
    id_number = models.CharField(max_length=15,primary_key=True)
    email = models.CharField(max_length=220)
    password = models.CharField(max_length=220,blank=True,null=True)

class AccountsApi(models.Model):
    id_number = models.CharField(max_length=15,primary_key=True)
    email = models.CharField(max_length=220)
    code = models.CharField(max_length=220,blank=True,null=True)


class NewOfferCode (models.Model):
    class Meta:
        unique_together = (('offer_code', 'sem_id','academic_year'))

    offer_code = models.CharField(max_length=225,default=None)
    days = ArrayField(models.CharField(max_length=220),default=list)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=225,default=None)
    subject_code = models.CharField(max_length=225,default=None)
    sem_id = models.CharField(max_length=225,default=None)
    academic_year = models.CharField(max_length=225,default=None)    

class OfferCode (models.Model):
    offer_code = models.CharField(max_length=15,primary_key=True)
    days = ArrayField(models.CharField(max_length=220),default=list)
    start_time = models.TimeField()
    end_time = models.TimeField()

class AllSubjects(models.Model):
    subject_code = models.CharField(max_length=225,primary_key=True)
    subject_title  = models.CharField(max_length=220) 
    units  = models.CharField(max_length=220)
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)

class Semester(models.Model):
    sem_id = models.CharField(max_length=225,primary_key=True)
    semester = models.CharField(max_length=225)

class SubjectWithSem(models.Model):
    id = models.CharField(max_length=225,primary_key=True)
    offer_code = models.CharField(max_length=225)
    sem_id = models.ForeignKey(Semester,on_delete=models.CASCADE)
    subject_code = models.ForeignKey(AllSubjects,on_delete=models.CASCADE)

class NewFacultyload(models.Model):
    offer_code = models.ForeignKey(OfferCode,on_delete=models.CASCADE,primary_key=True,related_name='organization')
    employee_id = models.ForeignKey(Faculty,on_delete=models.CASCADE,null=True)

class NewStudentsload(models.Model):
    id = models.CharField(max_length=220,primary_key=True)
    offer_code = models.ForeignKey(OfferCode,on_delete=models.CASCADE,null=True)
    studnumber = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)

class TeachersReferral(models.Model):
    studnumber= models.CharField(max_length=220)
    firstname = models.CharField(max_length=220)
    lastname = models.CharField(max_length=220)
    degree_program = models.CharField(max_length=220)
    subject_referred = models.CharField(max_length=220)
    reasons = models.CharField(max_length=10000)
    counselor = models.CharField(max_length=220)
    employeeid = models.CharField(max_length=220,blank=True, null=True)
    start_time = models.TimeField(blank=True,null=True)
    end_time = models.TimeField(blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    status = models.CharField(max_length=220,blank=True, null=True)
    BEHAVIOR_PROBLEM= (('CHEATING','CHEATING'),
                          ('TARDINESS','TARDINESS'),('DISRESPECTFUL','DISRESPECTFUL'),
                          ('ATTITUDE','ATTITUDE'),('USING GADGETS IN CLASS','USING GADGETS IN CLASS'),
                          ('GRUBBING','GRUBBING'))
    behavior_problem = models.CharField(max_length=220, choices=BEHAVIOR_PROBLEM,null=True,blank=True)


class SubjectOffered(models.Model):
    offer_no = models.CharField(max_length=220,primary_key=True)
    subject_no = models.CharField(max_length=220)
    subject_title = models.CharField(max_length=220)
    dayofsub =ArrayField(models.CharField(max_length=220),default=list,blank=True)
    start_time = models.TimeField(blank=True,null=True)
    end_time = models.TimeField(blank=True,null=True)
    units = models.CharField(max_length=220)



class Counselor(models.Model):
    PROGRAM_DESIGNATION = (('BSIT','BSIT'),
                          ('BSPT','BSPT'),('BSMT','BSMT'))
    employeeid = models.CharField(max_length=220,primary_key=True)
    firstname = models.CharField(max_length=220)
    lastname = models.CharField(max_length=220)
    program_designation = models.CharField(max_length=220, choices=PROGRAM_DESIGNATION,null=True,blank=True)



class Notification(models.Model):
    AUTOMATIC_REFERRAL = 'automatic_referral'
    MANUAL_REFERRAL = 'manual_referral'

    CHOICES = (
        (AUTOMATIC_REFERRAL,'automatic_referral'),
        (MANUAL_REFERRAL, 'manual_referral')
    )

    to_user = models.CharField(max_length=220,null=True,blank=True)
    notification_type = models.CharField(max_length=100, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=220,null=True,blank=True)
    # class Meta:
    #     ordering = ['-created_at']
