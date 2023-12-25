#Serializers are used to convert Django objects to Json/XML/etc. objects
from rest_framework import serializers
from .models import Company, Employee

#Create Serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta: #Using this class we specify what model we are using
        model = Company
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"