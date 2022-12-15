from django import forms
from expense import models


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = models.ExpenseModel
        fields = '__all__'

class ExpenseUpdateForm(forms.ModelForm):
    class Meta:
        model = models.ExpenseModel
        fields = '__all__'