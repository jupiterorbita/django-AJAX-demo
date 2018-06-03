from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^name_search$', views.name_search),
    url(r'^date_get$', views.date_get),
    url(r'^get_day$', views.get_day)
]