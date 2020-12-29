from django.shortcuts import render

#para importar csrf exam decorator para permitir a otros dominios acceder los metodos en el front end
from django.views.decorators.csrf import csrf_exempt

#tambien un Json parser para pasar datos al modelo de datos
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

#importamos los los modelos creados en la app y sus respectivos serializadores
from TicketApp.models import Tickets, Customers, Clients, Agency, User
from TicketApp.serializers import TicketSerializer, UserSerializer, AgencySerializer


# userApi - Creamos las vistas con el decorador csrf_exempt get, post, put y delete
@csrf_exempt
def userApi(request, Id=0):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data,safe=False)
    
    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Succesfull Add!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method =='PUT':
        user_data = JSONParser().parse(request)
        users = User.objects.get(UserId=user_data['UserId'])
        user_serializer = UserSerializer(users,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Succesfull Update!", safe=False)
        return JsonResponse("Fail Update", safe=False)

    elif request.method=='DELETE':
        users=User.objects.get(UserId=id)
        users.delete()
        return JsonResponse("X Succesfull Delete X")


# agencyApi - Creamos las vistas con el decorador csrf_exempt get, post, put y delete
@csrf_exempt
def agencyApi(request, id=0):
    if request.method == 'GET':
        agencies = Agency.objects.all()
        agency_serializer = AgencySerializer(agencies, many=True)
        return JsonResponse(agency_serializer.data,safe=False)
    
    elif request.method=='POST':
        agency_data = JSONParser().parse(request)
        agency_serializer = AgencySerializer(data=agency_data)
        if agency_serializer.is_valid():
            agency_serializer.save()
            return JsonResponse("Succesfull Add!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method =='PUT':
        agency_data = JSONParser().parse(request)
        agencies = Agency.objects.get(AgencyId=agency_data['id'])
        agency_serializer = AgencySerializer(agencies,data=agency_data)
        if agency_serializer.is_valid():
            agency_serializer.save()
            return JsonResponse("Succesfull Update!", safe=False)
        return JsonResponse("Fail Update", safe=False)

    elif request.method=='DELETE':
        agencies=Agency.objects.get(id=id)
        agencies.delete()
        return JsonResponse("X Succesfull Delete X")