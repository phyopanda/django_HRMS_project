from django import forms
from contract import models
from django.forms.widgets import DateInput

class ContractCreateForm(forms.ModelForm):
    class Meta:
        model = models.ContractModel
        fields = '__all__'
        widgets = {
        'start_date': DateInput(attrs={'type': 'date'}),
        'end_date': DateInput(attrs={'type': 'date'}),
        }
        

class ContractUpdateForm(forms.ModelForm):
    class Meta:
        model = models.ContractModel
        fields = '__all__'
        widgets = {
        'start_date': DateInput(attrs={'type': 'date'}),
        'end_date': DateInput(attrs={'type': 'date'}),
        }

