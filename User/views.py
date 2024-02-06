from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import response

@api_view(['POST'])
def User_Registration(request):
    
    return response.Response({'Status':200,'Message':'Data Received'})
