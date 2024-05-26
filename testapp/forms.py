from django import forms 
from .models import Mymodel
from phonenumber_field.formfields import PhoneNumberField
class MyForm(forms.ModelForm):
    resume=forms.FileField()
    mobile=PhoneNumberField()
    class Meta:
        model=Mymodel
        fields=['rollno','name','email','Dob','currentcompany', 'Exp_in_yr', 'salary','mobile','state',
    'resume']