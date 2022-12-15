from django.contrib import admin

# Register your models here.
from .models import ContractModel
from department.models import DepartmentModel

class ContractAdmin(admin.ModelAdmin):
	list_display = ['name','start_date','end_date','department_id','salary']

admin.site.register(ContractModel, ContractAdmin)