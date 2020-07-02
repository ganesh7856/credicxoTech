from django.shortcuts import render
from StateBank.models import Branch_Name


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import *
from .serializers import ApiSerializer

# Create your views here.


#Overiding Django's default 404 with custom JSON response
@api_view(['GET'])
def error_404(request, exception):
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def IFSC_View(request,ifsc,format=None):
        ifsc=ifsc.upper()
        try:
            ifsc = Branch_Name.objects.get(ifsc_code=ifsc)
        except IFSC.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ApiSerializer(ifsc)
            return Response(serializer.data)


@api_view(['GET'])
def BankName_CityNameView(request,bank,city,format=None):
    bank=bank.replace('-',' ').upper()
    city=city.replace('-',' ').upper()
    branches = Branch_Name.objects.filter(bank=bank,city=city).all()

    if bool(branches)==False:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApiSerializer(branches, many=True)
        return Response(serializer.data)
