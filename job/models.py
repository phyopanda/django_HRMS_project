from django.db import models

# Create your models here.
class JobModel(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    history = models.TextField(max_length=1000, verbose_name='History', default='No History')
    expected_employees = models.IntegerField(verbose_name='Expected Employees', default=0)

    def __str__(self):
        return self.name
    