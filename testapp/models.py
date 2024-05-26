
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError


class Mymodel(models.Model):
    State_choice=(
        ('Ap','Andhra Pradesh'),
        ('Up','Uttar Pradesh'),
        ('Mp','Madhya Pradesh'),
        ('Te','Telangana'),
        ('Ta','Tamilnadu'),
        ('ke','Kerala'),
        ('ka','Karnataka'),
        ('od','Odisha')
    )
    
    rollno = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    Dob = models.DateField()
    currentcompany = models.CharField(max_length=50)
    Exp_in_yr = models.IntegerField()
    salary = models.IntegerField()
    mobile = PhoneNumberField()
    state = models.CharField(max_length=2, choices=State_choice)
    resume = models.FileField(upload_to='resumes/') 
    
# Create your models here.
