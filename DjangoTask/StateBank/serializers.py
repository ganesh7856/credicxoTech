from rest_framework import serializers
from .models import Branch_Name

class ApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch_Name
        fields = ('bank','branch_name','ifsc_code','address','city','district','state')
