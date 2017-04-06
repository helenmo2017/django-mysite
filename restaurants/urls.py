from django.conf.urls import url
from restaurants.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^list/$', login_required(RestaurantsView.as_view()), name="restaurants_list"),
    url(r'^menu/(?P<pk>\d+)/$', login_required(MenuView.as_view()), name="menu"),
    url(r'^comment/(?P<pk>\d+)/$', login_required(CommentView.as_view()), name="comment"),
    url(r'^mos_menu/$', MenuView.as_view(), {'pk':3} ),
]
# urlpatterns = [
#     url(r'^list/$', restaurants_list, name="restaurants_list"),
#     url(r'^menu/(?P<id>\d{1,5})/$', restaurants.views.menu),
#     url(r'^comment/(\d{1,5})/$', restaurants.views.comment),
#     url(r'^mos_menu/$', restaurants.views.menu, {'id':3} ),
# ]