from django.contrib import admin

# Register your models here.
from .models import ExpenseModel
from employee.models import EmployeeModel

class ExpenseAdmin(admin.ModelAdmin):
	list_display = ['title','value','date','cash_out','employee']

admin.site.register(ExpenseModel, ExpenseAdmin)