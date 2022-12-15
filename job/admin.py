from django.contrib import admin

# Register your models here.
from .models import JobModel


class JobAdmin(admin.ModelAdmin):
	list_display = ['name','history','expected_employees']

admin.site.register(JobModel,JobAdmin)