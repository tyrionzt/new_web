from django.urls import path
from . import views

app_name = "[private]"
urlpatterns = [

    path(r'', views.index, name="index"),

    path(r'detail/', views.detail_journal, name="detail"),

    path(r'query/', views.query_journal, name="query"),

    path(r'like/', views.like_journal, name="like"),

]
