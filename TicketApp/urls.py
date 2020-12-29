from django.conf.urls import url

#llamamos  los views de la app
from TicketApp import views

    #agragamos las rutas de los views
urlpatterns=[
    url(r'^User/$',views.userApi),
    url(r'^Agency/$',views.agencyApi)
    # url(r'^Customer/$',views.customerApi),
    # url(r'^Client/$',views.clientApi),
    # url(r'^Tickets/$',views.ticketApi),
]