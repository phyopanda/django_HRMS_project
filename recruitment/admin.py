from django.contrib import admin

# Register your models here.
from .models import RecruitmentModel


class RecruitmentAdmin(admin.ModelAdmin):
	list_display = ['name','email','phone','address','birthday','image','education','skill','experience','objective','interest','position']

admin.site.register(RecruitmentModel, RecruitmentAdmin)