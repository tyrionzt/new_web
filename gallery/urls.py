from django.urls import path
from .views import *

app_name = "[gallery]"
urlpatterns = [
    path(r'', IndexView().get_queryset, name='index'),
    path(r'detail', IndexView().photo_detail, name='detail')
]
