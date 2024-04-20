from django.shortcuts import render,redirect
from .models import Employee,History
from .models import Salary
from django.contrib.auth import authenticate,login,logout
from .models import CalendarEvent
from datetime import datetime,timedelta
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    
    return render(request, "emp/home.html" )


def allemployees(request):
    emp = Employee.objects.all()
    return render(request, "emp/allemployees.html" , {"allemployees":emp})


def singleemployee(request, empid):
    return render(request, "emp/singleemployee.html")


def addemployee(request):
    if request.method == "POST":
        #take all the parameters from the form. by their names kept.
        employeeid = request.POST.get("employeeid")
        employeename = request.POST.get("employeename")
        employeeemail = request.POST.get("employeeemail")
        employeeaddress = request.POST.get("employeeaddress")
        employeemobilenumber = request.POST.get("employeemobilenumber")

        # create an object of the Employee model.
        e = Employee()
        e.employeeid = employeeid
        e.employeename = employeename
        e.email = employeeemail
        e.address = employeeaddress
        e.mobilenumber = employeemobilenumber
        e.save()
        return redirect("/allemployees")
    return render(request, "emp/addemployee.html")


def deleteemployee(request, empid):
    e = Employee.objects.get(pk = empid)
    e.delete()
    return redirect("allemployees")


def updateemployee(request, empid):
    e = Employee.objects.get(pk = empid)
    
    return render(request, "emp/updateemployee.html", {"singleemp": e})

def doupdateemployee(request, empid):
    updatedemployeeid           = request.POST.get('employeeid')
    updatedemployeename         = request.POST.get('employeename')
    updatedemployeeemail        = request.POST.get('employeeemail')
    updatedemployeeaddress      = request.POST.get('employeeaddress')
    updatedemployeemobilenumber = request.POST.get('employeemobilenumber')
    emp = Employee.objects.get(pk = empid)
    emp.employeeid   = updatedemployeeid
    emp.employeename = updatedemployeename
    emp.email        = updatedemployeeemail
    emp.address      = updatedemployeeaddress
    emp.mobilenumber = updatedemployeemobilenumber
    emp.save()
    return redirect("allemployees")


def salarydetails(request):
    emp = Salary.objects.all()
    return render(request, "emp/salarydetails.html" , {"salarydetails":emp})




def addsalary(request):
    emp = Salary.objects.all()
    if request.method == "POST":
        #take all the parameters from the form. by their names kept.
        employeeid = request.POST.get("employeeid")
        employeename = request.POST.get("employeename")
        employeeemail = request.POST.get("employeeemail")
        monthsalary = request.POST.get("monthsalary")
        workingdays = request.POST.get("workingdays")
        salaryyear = request.POST.get("salaryyear")
        annualsalary = request.POST.get("annualsalary")

        # create an object of the Salary model.
        e = Salary()
        e.employeeid = employeeid
        e.employeename = employeename
        e.email = employeeemail
        e.monthsalary = monthsalary
        e.workingdays = workingdays
        e.salaryyear = salaryyear
        e.annualsalary = annualsalary
        e.save()
        return redirect("/salarydetails")
    return render(request, "emp/addsalary.html" , {"addsalary":emp})


"""def login_page(request):
  if True:
    name=request.POST.get('username')
    if name =="keerthi":
    
     return redirect("/main")
  
    
    return render(request,"emp/login.html")"""

def login_page(request):
  if request.user.is_authenticated:
    return redirect("/main")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        
        
        return redirect("/allemployees")
      else:
        
        return redirect("/login")
    return render(request,"emp/login.html")
  
def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    
  return redirect("/")
  
def main(request):
    emp = Employee.objects.all()
    return render(request, "emp/main.html" , {"main":emp})

def login(request):
    return render(request, "emp/login.html")

def deletesalary(request, empid):
    e = Salary.objects.get(pk = empid)
    e.delete()
    return redirect("salarydetails")


def updatesalary(request, empid):
    e = Salary.objects.get(pk = empid)

    return render(request, "emp/updatesalary.html" ,{"singleemp": e})

def doupdatesalary(request, empid):
    updatedemployeeid           = request.POST.get('employeeid')
    updatedemployeename         = request.POST.get('employeename')
    updatedemployeeemail        = request.POST.get('employeeemail')
    updatedmonthsalary          = request.POST.get('monthsalary')
    updatedworkingdays          = request.POST.get('workingdays')
    updatedsalaryyear           = request.POST.get('salaryyear')
    updatedannualsalary         = request.POST.get('annualsalary')
    emp = Salary.objects.get(pk = empid)
    emp.employeeid   = updatedemployeeid
    emp.employeename = updatedemployeename
    emp.email        = updatedemployeeemail
    emp.monthsalary  = updatedmonthsalary
    emp.workingdays  = updatedworkingdays
    emp.salaryyear   = updatedsalaryyear
    emp.annualsalary = updatedannualsalary
    emp.save()
    return redirect("salarydetails")

def calendar(request):
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    if start_of_week > today:  # If today is Sunday, go back one week
        start_of_week -= timedelta(days=7)
    end_of_week = start_of_week + timedelta(days=6)
    weeks = []

    while start_of_week <= end_of_week:
        week = []
        for day in range(7):
            events = CalendarEvent.objects.filter(start_time__date=start_of_week)
            week.append((start_of_week, events))
            start_of_week += timedelta(days=1)
        weeks.append(week)

    return render(request, "emp/calendar.html", {'weeks': weeks})


def history(request):
    history = History.objects.all()
    return render(request, "emp/leave_history.html" , {"history":history})


def applyleave(request):
    if request.method == "POST":
        #take all the parameters from the form. by their names kept.
        employeeid = request.POST.get("employeeid")
        employeename = request.POST.get("employeename")
        employeeemail = request.POST.get("employeeemail")
        startdate = request.POST.get("startdate")
        enddate = request.POST.get("enddate")
        reason = request.POST.get("reason")
        

        # create an object of the Employee model.
        e = History()
        e.employeeid = employeeid
        e.employeename = employeename
        e.email = employeeemail
        e.startdate = startdate
        e.enddate = enddate
        e.reason = reason
        e.save()
        return redirect("/history")
    return render(request, "emp/request_leave.html")