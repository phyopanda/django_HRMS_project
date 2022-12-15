from django.db import models

# Create your models here.
from django.utils import timezone
from department import models as dm

class ContractModel(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    start_date = models.DateField(verbose_name='Start Date', default=timezone.now)
    end_date = models.DateField(verbose_name='End Date', default=timezone.now)
    salary = models.CharField(max_length=16,default='00,000.00')
    department_id = models.ForeignKey(dm.DepartmentModel, on_delete=models.CASCADE, default=None)

    def __str__(self): 
        return self.name