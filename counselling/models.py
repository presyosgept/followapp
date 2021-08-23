from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
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

class Referrals(models.Model):
    studnumber= models.CharField(max_length=220)
    subject_referred = models.CharField(max_length=220)
    counselor = models.CharField(max_length=220)
    employeeid = models.CharField(max_length=220,blank=True, null=True)
    start_time = models.TimeField(blank=True,null=True)
    end_time = models.TimeField(blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    status = models.CharField(max_length=220,blank=True, null=True)


class Students(models.Model):
    studnumber = models.CharField(max_length=220,primary_key=True)
    firstname = models.CharField(max_length=220,blank=True,null=True)
    lastname = models.CharField(max_length=220,blank=True,null=True)
    email = models.CharField(max_length=220,blank=True,null=True)
    course = models.CharField(max_length=220,blank=True,null=True)
    year = models.CharField(max_length=220,blank=True,null=True)
    role = models.CharField(max_length=220,blank=True,null=True)

class Teachersload(models.Model):
    employeeid = models.CharField(max_length=220,primary_key=True)
    firstname = models.CharField(max_length=220)
    lastname = models.CharField(max_length=220)
    external_email = models.CharField(max_length=220)
    role = models.CharField(max_length=220)

class SubjectOffered(models.Model):
    offer_no = models.CharField(max_length=220,primary_key=True)
    subject_no = models.CharField(max_length=220)
    subject_title = models.CharField(max_length=220)
    dayofsub =ArrayField(models.CharField(max_length=220),default=list,blank=True)
    start_time = models.TimeField(blank=True,null=True)
    end_time = models.TimeField(blank=True,null=True)
    units = models.CharField(max_length=220)
    

class Facultyload(models.Model):
    offer_no = models.CharField(max_length=220,primary_key=True)
    employeeid = models.CharField(max_length=220)

class Studentsload(models.Model):
    id = models.CharField(max_length=220,primary_key=True)
    offer_no = models.CharField(max_length=220)
    studnumber = models.CharField(max_length=220)

class Counselor(models.Model):
    PROGRAM_DESIGNATION = (('BSIT','BSIT'),
                          ('BSPT','BSPT'),('BSMT','BSMT'))
    employeeid = models.CharField(max_length=220,primary_key=True)
    firstname = models.CharField(max_length=220)
    lastname = models.CharField(max_length=220)
    program_designation = models.CharField(max_length=220, choices=PROGRAM_DESIGNATION,null=True,blank=True)

class CounselorSchedule(models.Model):
    SERVICE_OFFERED = (('CLASS','CLASS'),
                          ('COUNSELING','COUNSELING'),('OTHERS','OTHERS'))
    schedid = models.CharField(max_length=220,primary_key=True)
    time1 = models.TimeField(null=True,blank=True)
    time2 = models.TimeField(null=True,blank=True)
    service_offered = models.CharField(max_length=220,choices=SERVICE_OFFERED,null=True,blank=True)
    description = models.CharField(max_length=220,null=True,blank=True)

class StudentSchedule(models.Model):
    SCHEDULE = (('CLASS','CLASS'),
                          ('COUNSELING','COUNSELING'),('OTHERS','OTHERS'))
    schedid = models.CharField(max_length=220,primary_key=True)
    time1 = models.TimeField(null=True,blank=True)
    time2 = models.TimeField(null=True,blank=True)
    schedule = models.CharField(max_length=220,choices=SCHEDULE,null=True,blank=True)
    description = models.CharField(max_length=220,null=True,blank=True)

    
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
