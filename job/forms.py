from django import forms
from job import models

class JobCreateForm(forms.ModelForm):
    class Meta:
        model = models.JobModel
        fields = '__all__'

class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = models.JobModel
        fields = '__all__'