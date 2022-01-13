from rest_framework import serializers

from .models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'date_birth', 'gender', 'zip_code', 'house_number', 'telephone', 'email', 'notes']
