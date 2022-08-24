from django.db import models
from job import models as jm

# Create your models here.
class DepartmentModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    history = models.TextField(max_length=1000, verbose_name='History', default='No History')
    job_id = models.ForeignKey(jm.JobModel, on_delete=models.CASCADE, default=None)
    expected_employees = models.IntegerField(verbose_name='Expected Employees', default=0)

    def __str__(self):
        return self.name
