from django.db import models

# Create your models here.
from django.utils import timezone
from job import models as jm

class ContractModel(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    start_date = models.DateField(verbose_name='Start Date', default=timezone.now)
    end_date = models.DateField(verbose_name='End Date', default=timezone.now)
    salary = models.CharField(max_length=16,default='00,000.00')
    job_id = models.ManyToManyField(jm.JobModel)

    def __str__(self): 
        return self.name