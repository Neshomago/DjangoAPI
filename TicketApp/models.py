from django.db import models

# Create your models here.
# PRI = (
#     ('0', 'Low'),
#     ('1', 'Medium'),
#     ('2', 'High')
# )


# REQT = (
#     ('0', 'Instalation'),
#     ('1', 'Integration'),
#     ('2', 'Maintenance'),
#     ('3', 'Uninstall'),
#     ('4', 'Support'),
#     ('5', 'Integration Delivery'),
#     ('6', 'Maintenance Delivery')
# )


# class Tickets(models.Model):
#     TicketId = models.AutoField(primary_key=True)
#     SalesPoint = models.CharField(max_length=255)
#     RequestType = models.CharField(max_length=1, choices=REQT)
#     Priority = models.CharField(max_length=1, choices=PRI)
#     TicketCode = models.CharField(max_length=100)
#     Client = models.CharField(max_length=200)
#     TicketDescrp = models.CharField(max_length=255)
#
#    objects = models.Manager()
#
#
# class Customers(models.Model):
#     CustomerID = models.AutoField(primary_key=True)
#     CustomerName = models.CharField(max_length=200)
#     CustomerIVA = models.IntegerField()
#     CustomerAddress = models.CharField(max_length=200)
#     CustomerEmail = models.CharField(max_length=255)
#     CustomerPhone = models.CharField(max_length=20)
#
#     objects = models.Manager()
#
#
# class Clients(models.Model):
#     ClientName = models.CharField(max_length=255)
#     ClientSurname = models.CharField(max_length=255)
#     ClientFiscal = models.CharField(max_length=20)
#     ClientContact = models.CharField(max_length=200)
#     ClientContactAddress = models.CharField(max_length=200)
#     ClientContactEmail = models.CharField(max_length=255)
#     ClientContactPhone = models.CharField(max_length=20)
#
#     objects = models.Manager()
#
#
# class Agency(models.Model):
#     id = models.AutoField(primary_key=True)
#     AgencyName = models.CharField(max_length=200)
#     AgencyIVA = models.IntegerField()
#     AgencyManagerId = models.CharField(max_length=20)
#     AgencyCertification = models.CharField(max_length=20)
#     AgencyAddress = models.CharField(max_length=200)
#     AgencyEmail = models.CharField(max_length=255)
#     AgencyPhone = models.CharField(max_length=20)
#
#     objects = models.Manager()
#
#
# class User(models.Model):
#     UserId = models.AutoField(primary_key=True)
#     UserName = models.CharField(max_length=200)
#     UserEmail = models.CharField(max_length=255)
#     UserPassword = models.CharField(max_length=12)
#     UserRole = models.CharField(max_length=5)
#
#     objects = models.Manager()


NMSTCKT = (
    ('INS', 'Instalation'),
    ('INT', 'Integration'),
    ('MAN', 'Maintenance'),
    ('DIS', 'Uninstall'),
    ('SUP', 'Support'),
    ('IND', 'Integration Delivery'),
    ('MND', 'Maintenance Delivery')
)

NMSTCKTSTA = (
    ('OPENED', 'Open Ticket'),
    ('MANAGING', 'Managing Ticket'),
    ('WORKING', 'Working Ticket'),
    ('RESOLVED', 'Resolved Ticket'),
    ('REJECTED', 'Rejected Ticket'),
    ('ABORTED', 'Aborted Operation')
)


PRIORY = (
    ('LOW', 'Low Priority'),
    ('NORMAL', 'Normal Priority'),
     ('HIGH', 'High Priority')
)


class nemesis_n_ticket_model(models.Model):
    createdBy = models.CharField(max_length=20)
    type = models.CharField(max_length=3, choices=NMSTCKT)
    customerId = models.CharField(max_length=20)
    creationDate = models.DateField()
    status = models.CharField(max_length=8, choices=NMSTCKTSTA)
    priority = models.CharField(max_length=6, choices=PRIORY)
    agencyId = models.CharField(max_length=20)
    description = models.TextField()
    id = models.CharField(max_length=20, primary_key=True)
    version = models.IntegerField()
    code = models.CharField(max_length=45)

    objects = models.Manager()


class nemesis_n_agency_model(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=200,null=True)
    managerId = models.CharField(max_length=45, null=True)
    vat = models.CharField(max_length=16)
    email = models.CharField(max_length=45, null=True)
    phone = models.CharField(max_length=45)
    certification = models.CharField(max_length=45, null=True)
    customerId = models.CharField(max_length=20,null=True)
    moreInfo = models.CharField(max_length=250, default='')
    id = models.CharField(max_length=20, primary_key=True)
    version = models.IntegerField()

    objects = models.Manager()


class nemesis_n_customer_model(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=250)
    vat = models.CharField(max_length=16)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    id = models.CharField(max_length=20, primary_key=True)
    version = models.IntegerField()

    objects = models.Manager()


class nemesis_n_contact_model(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    taxCode = models.CharField(max_length=16)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=45)
    user = models.CharField(max_length=20)
    customerId = models.CharField(max_length=20)
    id = models.CharField(max_length=20, primary_key=True)
    version = models.IntegerField()

    objects = models.Manager()
