from django import forms
from department import models

class DepartmentCreateForm(forms.ModelForm):
    class Meta:
        model = models.DepartmentModel
        fields = '__all__'

class DepartmentUpdateForm(forms.ModelForm):
    class Meta:
        model = models.DepartmentModel
        fields = '__all__'