from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^list/$', restaurants_list, name="restaurants_list"),
    url(r'^menu/(?P<id>\d{1,5})/$', menu, name="menu"),
    url(r'^comment/(\d{1,5})/$', comment, name="comment"),
    url(r'^mos_menu/$', menu, {'id':3} ),
]
# urlpatterns = [
#     url(r'^list/$', restaurants_list, name="restaurants_list"),
#     url(r'^menu/(?P<id>\d{1,5})/$', restaurants.views.menu),
#     url(r'^comment/(\d{1,5})/$', restaurants.views.comment),
#     url(r'^mos_menu/$', restaurants.views.menu, {'id':3} ),
# ]