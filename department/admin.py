from django.contrib import admin

# Register your models here.
from .models import DepartmentModel
from job.models import JobModel

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['name','history','job_id','expected_employees']

admin.site.register(DepartmentModel, DepartmentAdmin)