from django.contrib import admin
from .models import User_Registration

class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('User_Id', 'Full_Name', 'Username', 'Email_Address', 'Phone_Number', 'Date_Of_Registration')
    search_fields = ['User_Id', 'Full_Name', 'Username', 'Email_Address', 'Phone_Number']
    #list_filter = ('Organization_Name', 'State', 'District', 'City', 'ABC_ID')

admin.site.register(User_Registration, UserRegistrationAdmin)
