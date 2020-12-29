from django.conf.urls import url

#llamamos  los views de la app
from TicketApp import views

urlpatterns=[
    #agragamos las rutas de los views
    url(r'^User/$',views.userApi),
    url(r'^Agency/$',views.userApi),
    url(r'^Customer/$',views.userApi),
    url(r'^Client/$',views.userApi),
    url(r'^Tickets/$',views.userApi),

]