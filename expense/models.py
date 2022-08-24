from django.db import models

# Create your models here.
from django.utils import timezone
from employee import models as em

class ExpenseModel(models.Model):
    title = models.CharField(max_length=20, verbose_name='Name')
    value = models.CharField(max_length=16,default='00,000.00')
    date = models.DateTimeField(default=timezone.now)
    cash_out = models.BooleanField(default=False)
    employee = models.ForeignKey(em.EmployeeModel, on_delete=models.CASCADE, default=None)
	
    def __str__(self):
        return self.name