# yourapp/serializers.py
from rest_framework import serializers
from .models import User_Credentials

class UserCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Credentials
        fields = '__all__'
