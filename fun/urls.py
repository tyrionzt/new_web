from django.urls import path
from . import views

app_name = "[fun]"
urlpatterns = [

    path(r'', views.index),

    path(r'show_recode/', views.show_recode),

    path(r'download/', views.download_game),

    path(r'action/', views.start_action, name="action"),
]
