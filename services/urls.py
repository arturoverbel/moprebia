from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<frecuencia>\d+)/(?P<porcentaje>\d+)/$$', views.getData, name='getData'),
]