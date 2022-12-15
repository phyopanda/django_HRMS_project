from django import forms
from employee import models
from django.forms.widgets import DateInput


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = models.EmployeeModel
        fields = '__all__'
        widgets = {
        'birthday': DateInput(attrs={'type': 'date'}),
        }
class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = models.EmployeeModel
        fields = '__all__'
        widgets = {
        'birthday': DateInput(attrs={'type': 'date'}),
        }