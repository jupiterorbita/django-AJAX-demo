from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^all.json$', views.all_json),
    url(r'^all.html$', views.all_html),
    url(r'^find$', views.find),
    url(r'^find_last$', views.find_last),
    url(r'^find_age$', views.find_age),
    url(r'^create$', views.create)
]