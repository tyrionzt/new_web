from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index),

    url(r'^show_recode/$', views.show_recode),

    url(r'^download/$', views.download_game)
]
