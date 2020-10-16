from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', IndexView().get_queryset, name='index'),
    url(r'^detail$', IndexView().photo_detail, name='detail')
]