# Generated by Django 3.1.4 on 2024-02-06 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Id', models.IntegerField()),
                ('Organization_Name', models.CharField(max_length=100)),
                ('Date_Of_Registration', models.DateField()),
                ('Full_Name', models.CharField(max_length=50)),
                ('Username', models.CharField(max_length=20)),
                ('Email_Address', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=30)),
                ('Phone_Number', models.IntegerField()),
                ('Date_Of_Birth', models.DateField()),
                ('User_Photo', models.FileField(default=None, upload_to='UserRegistration/UserPhoto/')),
                ('Residence_Address', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=20)),
                ('District', models.CharField(max_length=20)),
                ('Permanent_Address', models.CharField(max_length=50)),
                ('Taluka', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
                ('Pincode', models.IntegerField()),
                ('Aadharcard_No', models.IntegerField()),
                ('Aadharcard_File', models.FileField(default=None, upload_to='UserRegistration/Aadharcard/')),
                ('Driving_License', models.CharField(max_length=16)),
                ('Driving_License_File', models.FileField(default=None, upload_to='UserRegistration/DrivingLicense/')),
                ('Uni_Id_Card_Number', models.CharField(max_length=12)),
                ('Uni_Id_File', models.FileField(default=None, upload_to='UserRegistration/UniIdFile/')),
                ('Pan_Card_Number', models.CharField(max_length=10)),
                ('Pan_Card_File', models.FileField(default=None, upload_to='UserRegistration/PanCard')),
                ('ABC_ID', models.IntegerField()),
                ('ABC_ID_File', models.FileField(default=None, upload_to='UserRegistration/ABCIdFile')),
                ('Voting_Card_Number', models.CharField(max_length=12)),
                ('Voting_Card_File', models.FileField(default=None, upload_to='UserRegistration/VotingCard')),
            ],
        ),
    ]
