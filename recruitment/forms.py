from django import forms
from recruitment import models
from django.forms.widgets import DateInput

class RecruitmentCreateForm(forms.ModelForm):
    class Meta:
        model = models.RecruitmentModel
        fields = '__all__'
        widgets = {
        'birthday': DateInput(attrs={'type': 'date'}),
        }

class RecruitmentUpdateForm(forms.ModelForm):
    class Meta:
        model = models.RecruitmentModel
        fields = '__all__'
        widgets = {
        'birthday': DateInput(attrs={'type': 'date'}),
        }