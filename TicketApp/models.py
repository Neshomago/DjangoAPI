from django.db import models

# Create your models here.
PRI = (
    ('0', 'Low'),
    ('1', 'Medium'),
    ('2', 'High')
)


REQT = (
    ('0', 'Instalation'),
    ('1', 'Integration'),
    ('2', 'Maintenance'),
    ('3', 'Uninstall'),
    ('4', 'Support'),
    ('5', 'Integration Delivery'),
    ('6', 'Maintenance Delivery')
)


class Tickets(models.Model):
    TicketId = models.AutoField(primary_key=True)
    SalesPoint = models.CharField(max_length=255)
    RequestType = models.CharField(max_length=1, choices=REQT)
    Priority = models.CharField(max_length=1, choices=PRI)
    TicketCode = models.CharField(max_length=100)
    Client = models.CharField(max_length=200)
    TicketDescrp = models.CharField(max_length=255)

    objects = models.Manager()


class Customers(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=200)
    CustomerIVA = models.IntegerField()
    CustomerAddress = models.CharField(max_length=200)
    CustomerEmail = models.CharField(max_length=255)
    CustomerPhone = models.CharField(max_length=20)

    objects = models.Manager()


class Clients(models.Model):
    ClientName = models.CharField(max_length=255)
    ClientSurname = models.CharField(max_length=255)
    ClientFiscal = models.CharField(max_length=20)
    ClientContact = models.CharField(max_length=200)
    ClientContactAddress = models.CharField(max_length=200)
    ClientContactEmail = models.CharField(max_length=255)
    ClientContactPhone = models.CharField(max_length=20)

    objects = models.Manager()


class Agency(models.Model):
    id = models.AutoField(primary_key=True)
    AgencyName = models.CharField(max_length=200)
    AgencyIVA = models.IntegerField()
    AgencyManagerId = models.CharField(max_length=20)
    AgencyCertification = models.CharField(max_length=20)
    AgencyAddress = models.CharField(max_length=200)
    AgencyEmail = models.CharField(max_length=255)
    AgencyPhone = models.CharField(max_length=20)

    objects = models.Manager()


class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=200)
    UserEmail = models.CharField(max_length=255)
    UserPassword = models.CharField(max_length=12)
    UserRole = models.CharField(max_length=5)

    objects = models.Manager()
