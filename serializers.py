from rest_framework import serializers
from .models import Clients

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('pk',
                  'first_name',
                  'last_name',
                  'email_address',
                  'created')
