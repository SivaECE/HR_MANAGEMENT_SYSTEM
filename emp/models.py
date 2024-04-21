from django.db import models
from datetime import datetime
import os
from django.contrib.auth.models import User
def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

# Create your models here.




class Salary(models.Model):
    employeeid    = models.CharField(max_length=100)
    employeename  = models.CharField(max_length=50)
    email         = models.CharField(max_length=50)
    monthsalary   = models.CharField(max_length=50)
    workingdays   = models.CharField(max_length=50)
    salaryyear    = models.CharField(max_length=50)
    annualsalary  = models.CharField(max_length=50)
    


class CalendarEvent(models.Model):
    event_name = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=datetime.now)
    end_time   = models.DateTimeField(default=datetime.now)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.event_name
    


class History(models.Model):
    employeeid    = models.CharField(max_length=100)
    employeename  = models.CharField(max_length=50)
    email         = models.CharField(max_length=50)
    startdate     = models.DateField()
    enddate       = models.DateField()
    reason        = models.CharField(max_length=50)
    status        = models.CharField(max_length=50)   

class Employeedetails(models.Model):
    employeeid       = models.CharField(max_length=100)
    image            =models.ImageField(upload_to=getFileName,null=True,blank=True)
    employeename     = models.CharField(max_length=50)
    email            = models.CharField(max_length=50)
    dateofbirth      = models.CharField(max_length=50)
    bloodgroup         = models.CharField(max_length=50)
    gender         = models.CharField(max_length=50)
    maritalstatus         = models.CharField(max_length=50)
    aadharnumber        = models.CharField(max_length=50)
    pannumber         = models.CharField(max_length=50)
    address       = models.CharField(max_length=50)
    city         = models.CharField(max_length=50)
    state         = models.CharField(max_length=50)
    pincode         = models.CharField(max_length=50)
    mobilenumber  = models.CharField(max_length=50)
