from rest_framework import serializers
from TicketApp.models import nemesis_n_customer_model, nemesis_n_ticket_model, nemesis_n_agency_model, nemesis_n_contact_model


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('UserId', 'UserName', 'UserEmail', 'UserPassword', 'UserRole')


# class TicketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tickets
#         fields = ('TicketId', 'SalesPoint', 'RequestType', 'Priority', 'TicketCode', 'Client', 'TicketDescrp')


# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Clients
#         fields = ('ClientName', 'ClientSurname', 'ClientFiscal', 'ClientContact', 'ClientContactAddress',
#                   'ClientContactEmail', 'ClientContactPhone')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = nemesis_n_customer_model
        fields = ('name', 'address', 'vat', 'email', 'phone', 'id', 'version')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = nemesis_n_contact_model
        fields = ('name', 'surname', 'taxCode', 'address', 'phone', 'user', 'customerId', 'id', 'version')


class NemesisTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = nemesis_n_ticket_model
        fields = ('createdBy', 'type', 'customerId', 'creationDate', 'status', 'priority', 'agencyId', 'description',
                  'id', 'version', 'code')


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = nemesis_n_agency_model
        fields = ('name', 'address', 'managerId', 'vat', 'email', 'phone', 'certification', 'customerId', 'moreInfo', 'id', 'version')