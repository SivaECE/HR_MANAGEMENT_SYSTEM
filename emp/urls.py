
from django.urls import path
from . import views 



urlpatterns = [
    path("",                              views.home,            name="home"),
    path("allemployees/",                 views.allemployees,    name="allemployees"),
    path("singleemployee/<int:empid>/",   views.singleemployee,  name="singleemployee"),
    path("addemployee/",                  views.addemployee,     name="addemployee"),
    path("deleteemployee/<int:empid>/",   views.deleteemployee,  name="deleteemployee"),
    path("updateemployee/<int:empid>/",   views.updateemployee,  name="updateemployee"),
    path("doupdateemployee/<int:empid>/", views.doupdateemployee,name="doupdateemployee"),
    path("login/",                        views.login_page,      name="login"),
    path("salarydetails/",                views.salarydetails,   name="salarydetails"),
    path("calendar/",                     views.calendar,        name="calendar"),
    path("addsalary/",                    views.addsalary,       name="addsalary"),
    path("deletesalary/<int:empid>/",     views.deletesalary,    name="deletesalary"),
    path("updatesalary/<int:empid>/",     views.updatesalary,    name="updatesalary"),
    path("doupdatesalary/<int:empid>/",   views.doupdatesalary,  name="doupdatesalary"),
    path("main/",                         views.main,            name="main"),
    path("logout/",                       views.logout_page,     name="logout"),
    
    path("applyleave/",                 views.applyleave, name="applyleave"),
    path("history/",                 views.history, name="history"),
   

]
