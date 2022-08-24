from django.db import models
import random
# Create your models here.

from django.utils import timezone
from contract import models as cm
from department import models as dm

class EmployeeModel(models.Model):
	emp_id = models.CharField(max_length=70, default='emp'+str(random.randrange(100,999,1)))
	name = models.CharField(max_length=20, verbose_name='Name')
	birthday=models.DateField(auto_now=False, null=True, blank=True)
	address = models.TextField(max_length=100, verbose_name='Address')
	phone = models.CharField(max_length=15, verbose_name='Phone')
	email = models.EmailField(max_length=125, verbose_name='Email')
	image = models.ImageField(upload_to='imgs/', default=None, null=True, blank=True)
	salary = models.CharField(max_length=16,default='00,000.00')
	joined = models.DateTimeField(default=timezone.now)
	contract = models.ForeignKey(cm.ContractModel, on_delete=models.CASCADE, default=None)
	department = models.ForeignKey(dm.DepartmentModel, on_delete=models.CASCADE, default=None)