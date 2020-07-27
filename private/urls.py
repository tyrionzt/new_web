from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index),

    url(r'detail/', views.detail_journal, name="detail"),

    url(r'update/', views.update_journal, name="update"),

    url(r'delete/', views.delete_journal, name="delete"),

]
