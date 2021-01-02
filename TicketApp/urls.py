from django.urls import path
from django.conf.urls import url

# llamamos  los views de la app
from TicketApp import views

    # agragamos las rutas de los views
urlpatterns=[
    url(r'^User/$', views.userApi),
    url(r'User/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
    url(r'^Agency/$', views.agencyApi),
    url(r'^Customer/$', views.customerApi),
    # url(r'^Client/$',views.clientApi),
    url(r'^Tickets/$', views.ticketApi),
    url(r'Tickets/(?P<pk>[0-9]+)$', views.TicketDetail.as_view()),
]