from django.urls import path
from django.conf.urls import url

# llamamos  los views de la app
from TicketApp import views

    # agragamos las rutas de los views
urlpatterns = [
    #url(r'^User/$', views.userApi),
    #url(r'User/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
    url(r'^agency/$', views.agencyApi),
    url(r'^customer/$', views.customerApi),
    url(r'^contact/$', views.contactApi),
    url(r'^tickets/$', views.ticketApi),
    url(r'tickets/(?P<pk>[0-9]+)$', views.TicketDetail.as_view()),
    url(r'^agency/(?P<pk>[0-9]+)$', views.AgencyDetail.as_view()),
    url(r'^customer/(?P<pk>[0-9]+)$', views.CustomerDetail.as_view()),
    url(r'^contact/(?P<pk>[0-9]+)$', views.ContactDetail.as_view()),
]