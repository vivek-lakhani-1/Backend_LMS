from django.contrib import admin
from .models import User_Registration,User_Credentials

class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('User_Id', 'Full_Name', 'Username', 'Email_Address', 'Phone_Number', 'Date_Of_Registration')
    search_fields = ['User_Id', 'Full_Name', 'Username', 'Email_Address', 'Phone_Number']
    list_filter = ('Organization_Name', 'State', 'District', 'City', 'ABC_ID')

class UserCredentialsAdmin(admin.ModelAdmin):
    list_display = ('User_Id','User_Name','User_Email')
    list_filter = ('User_Id','User_Name','User_Email')
admin.site.register(User_Credentials,UserCredentialsAdmin)
admin.site.register(User_Registration, UserRegistrationAdmin)
