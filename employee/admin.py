from django.contrib import admin

# Register your models here.
from .models import EmployeeModel
from contract.models import ContractModel
from department.models import DepartmentModel

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['name','emp_id','salary','address','email', 'birthday', 'image','contract','department']

admin.site.register(EmployeeModel, EmployeeAdmin)