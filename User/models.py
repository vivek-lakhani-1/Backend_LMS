from django.db import models





class User_Credentials(models.Model):
    User_Id = models.BigAutoField(primary_key=True)
    User_Name = models.CharField(max_length=255)
    User_Email = models.EmailField()
    User_Password = models.TextField()
    def __str__(self):
        return self.User_Name


# Create your models here.
class User_Registration(models.Model):
    User_Id = models.OneToOneField(User_Credentials, on_delete=models.CASCADE)
    Organization_Name = models.CharField(max_length=100)
    Date_Of_Registration = models.DateField()
    Full_Name = models.CharField(max_length=50)
    Username = models.CharField(max_length=20)
    Email_Address = models.EmailField(max_length=50)
    Password = models.CharField(max_length=30)
    Phone_Number = models.IntegerField()
    Date_Of_Birth = models.DateField()
    User_Photo = models.FileField(upload_to="UserRegistration/UserPhoto/",default=None)
    Residence_Address = models.CharField(max_length=50)
    State = models.CharField(max_length=20)
    District = models.CharField(max_length=20)
    Permanent_Address = models.CharField(max_length=50)
    Taluka = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Pincode = models.IntegerField()
    Aadharcard_No = models.IntegerField()
    Aadharcard_File = models.FileField(upload_to="UserRegistration/Aadharcard/",default=None)
    Driving_License = models.CharField(max_length=16)
    Driving_License_File = models.FileField(upload_to="UserRegistration/DrivingLicense/",default=None)
    Uni_Id_Card_Number = models.CharField(max_length=12)
    Uni_Id_File = models.FileField(upload_to="UserRegistration/UniIdFile/",default=None)
    Pan_Card_Number = models.CharField(max_length=10)
    Pan_Card_File = models.FileField(upload_to="UserRegistration/PanCard",default=None)
    ABC_ID = models.IntegerField()
    ABC_ID_File = models.FileField(upload_to="UserRegistration/ABCIdFile",default=None)
    Voting_Card_Number = models.CharField(max_length=12)
    Voting_Card_File = models.FileField(upload_to="UserRegistration/VotingCard",default=None)
    def __str__(self):
        return self.Full_Name