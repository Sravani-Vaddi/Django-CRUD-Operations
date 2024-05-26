# Generated by Django 4.2.5 on 2024-03-11 01:59

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Dob', models.DateField()),
                ('currentcompany', models.CharField(max_length=50)),
                ('Exp_in_yr', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('state', models.CharField(choices=[('Ap', 'Andhra Pradesh'), ('Up', 'Uttar Pradesh'), ('Mp', 'Madhya Pradesh'), ('Te', 'Telangana'), ('Ta', 'Tamilnadu'), ('ke', 'Kerala'), ('ka', 'Karnataka'), ('od', 'Odisha')], max_length=2)),
                ('resume', models.FileField(upload_to='resumes/')),
            ],
        ),
    ]
