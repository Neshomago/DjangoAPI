# DjangoAPI

Guia base
https://www.youtube.com/watch?v=1Hc7KlLiU9w


Install python 3.9
Install Django
Pip3 install mysqlclient

Trabajamos bajo la carpeta nemesis-appv2

creamos un entorno virtual python y trabajamos en el:
	$ python3 -m venv nms

Activate virtual environment source nms/bin/activate
dentro del entorno virtual instalamos dependencias
$ pip3 Install Djangorestframework

create Django project:
	$ django-admin startproject DjangoAPI
	
Configurar settings.py para habilitar mysql 
  - link de referencia de activacion: https://medium.com/@omaraamir19966/connect-django-with-mysql-database-f946d0f6f9e3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodatabase',
        'USER': 'dbadmin',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Luego migrar los cambios
python3 manage.py migrate

Install cors
Pip3 install django-cors-headers

Settings.py
	añadir una linea en Installed_aps
	‘corsheaders’,
	
	añadir una linea en MIDDLEWARE 
	‘corsheaders.middleware.CorsMiddleWare’

	antes de MIDDLEWARE agregar
		CORS_ORIGIN_ALLOW_ALL = True


Crear una app mediante manage,py
	python3 manage.py startapp TicketApp


Editar models.py de la TicketApp, Customers, Clientes, User
	class Tickets(models.Model):
    TicketId = models.AutoField(primary_key=True)
    SalesPoint = models.CharField(max_length=255)
    RequestType = models.CharField(max_length=20)
    Priority = models.CharField(max_length=10)
    TicketCode = models.CharField(max_length=255)
    Client = models.CharField(max_length=255)
    TicketDescrp =  models.CharField(max_length=255)

Create tables 
	$ python3 manage.py makemigrations TicketApp
	Esto crea un archivo intermediario en la carpeta migrations
	que contiene los cambios que van en el archivo de la base de datos

Para asegurar esto necesitamos ejecutar el commit en python
	$ python3 manage.py migrate TicketApp

Crear serializadores en la App para convertir tipos a json y viceversa
	crear un nuevo archivo serializers.py
	importamos serializers from rest_framework

	from rest_framework import serializers
from TicketApp.models import User#, Clients, Tickets, Customers, Agency

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId',
        'UserName', 'UserEmail','UserPassword','UserRole')

Instalar pylant-django si da problemas en la siguiente parte:
	$pip3 install pylint-django
Luego en la app en views.py
Vamos a colocar API para la pantalla User (get, put, post, delete)

#para importar csrf exam decorator para permitir a otros dominios acceder los metodos en el front end
from django.views.decorators.csrf import csrf_exempt

#tambien un Json parser para pasar datos al modelo de datos
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

#importamos los los modelos creados en la app y sus respectivos serializadores
from TicketApp.models import Tickets, Customers, Clients, Agency, User
from TicketApp.serializers import TicketSerializer, UserSerializer


# Creamos las vistas con el decorador csrf_exempt
@csrf_exempt
def userApi(request, Id=0):
    if request.methor == 'GET':
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

Crear archivo urls.py en TicketApp
	Agregamos las siguientes rutas de los views
	
from django.conf.urls import url
from TicketApp import views

urlpatterns=[
    url(r'^User/$',views.userApi),
    url(r'^Agency/$',views.userApi),
    url(r'^Customer/$',views.userApi),
    url(r'^Client/$',views.userApi),
    url(r'^Tickets/$',views.userApi),

]

Y tambien en los urls.py del proyecto Django

from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('TicketApp.urls'))
]
