from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name="index"),

    url(r'detail/', views.detail_journal, name="detail"),

    url(r'query/', views.query_journal, name="query"),

    url(r'like/', views.like_journal, name="like"),

]
