from django.contrib import admin
from .models import Employeedetails
from .models import Salary
from .models import CalendarEvent
from .models import History

# Register your models here.
 
admin.site.register(Employeedetails)
admin.site.register(Salary)
admin.site.register(CalendarEvent)
admin.site.register(History)
