from rest_framework import serializers
from TicketApp.models import User, Clients, Tickets, Customers, Agency


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'UserName', 'UserEmail', 'UserPassword', 'UserRole')


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('TicketId', 'SalesPoint', 'RequestType', 'Priority', 'TicketCode', 'Client', 'TicketDescrp')


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = ('AgencyName', 'AgencyIVA', 'AgencyManagerId', 'AgencyCertification', 'AgencyAddress',
                  'AgencyEmail', 'AgencyPhone')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('ClientName', 'ClientSurname', 'ClientFiscal', 'ClientContact', 'ClientContactAddress',
                  'ClientContactEmail', 'ClientContactPhone')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('CustomerID', 'CustomerName', 'CustomerIVA', 'CustomerAddress', 'CustomerEmail', 'CustomerPhone')
