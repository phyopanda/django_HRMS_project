from django.db import models

from django.utils import timezone
# Create your models here.
class RecruitmentModel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=40)
    birthday=models.DateField(auto_now=False, null=True, blank=True)
    image = models.ImageField(upload_to='imgs/', default=None, null=True, blank=True)
    education = models.CharField(max_length=1000)
    skill = models.CharField(max_length=500)
    experience = models.CharField(max_length=1000)
    objective = models.CharField(max_length=500)
    interest = models.CharField(max_length=500)
    position = models.CharField(max_length=15)

    def __str__(self):
        return self.name +' - '+self.position
