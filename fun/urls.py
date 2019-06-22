from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index),

    url(r'^show_rcode/$', views.show_rcode),

    url(r'^download/$', views.download_game)
]