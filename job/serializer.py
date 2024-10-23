from rest_framework import serializers
from .models import EmailList ,JobDetails,Address,Location

class EmailListSerializer(serializers.ModelSerializer):
      class Meta:
        model = EmailList
        fields = '__all__'

class JobDetailsSerializer(serializers.ModelSerializer):
      class Meta:
        model = JobDetails
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
      class Meta:
        model =  Address
        fields = '__all__'



class LocationSerializer(serializers.ModelSerializer):
      class Meta:
        model =  Location
        fields = '__all__'


