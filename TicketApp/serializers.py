from rest_framework import serializers
from TicketApp.models import User, Clients, Tickets, Customers, Agency

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId','UserName', 'UserEmail','UserPassword','UserRole')

class TicketSerializer (serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('TicketId','SalesPoint','RequestType','Priority','TicketCode','Client','TicketDescrp')