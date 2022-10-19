from dataclasses import fields
from django import forms
from .models import Opdetails

GENDE_CHOICE=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)

class Online_consultForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDE_CHOICE,widget=forms.RadioSelect)
    class Meta:
        model=Opdetails
        fields=['name','age','gender','date','doctor_type','mobile']
    widgets={
        'name':forms.TextInput(attrs={'class': 'input input-bordered input-secondary w-full max-w-xs rounded-lg'}),
        'age':forms.NumberInput(attrs={'class': 'input input-bordered input-secondary w-full max-w-xs rounded-lg'}),
        'gender':forms.TextInput(attrs={'class': 'input input-bordered input-secondary w-full max-w-xs rounded-lg'}),
        'date':forms.DateInput(attrs={'class': 'input input-bordered input-secondary w-full max-w-xs rounded-lg'}),
        'doctor_type':forms.Select(attrs={'class': 'input input-bordered input-secondary w-full max-w-xs rounded-lg'}),
        'mobile':forms.NumberInput(attrs={'class': 'input input-bordered input-secondary w-full max-w-xs rounded-lg'}),
            }    