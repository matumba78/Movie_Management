from django.conf.urls import url,include
from django.contrib import admin
from .views import Newmovie,Searchbygenre,MonthlyRelease,Searchbydirector,Search,Actorstats

urlpatterns=[

#url(r'^update/',Updatemovie.as_view(),name='b'),
url(r'^newmovie/',Newmovie.as_view(),name='b'),
url(r'^genre/(?P<genre>\D+)',Searchbygenre.as_view(),name='r'),
url(r'byyear/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})$',MonthlyRelease.as_view(),name='c'),
url(r'^director/(?P<director>\D+)',Searchbydirector.as_view(),name='t'),
url(r'^search/(?P<movie>\D+)',Search.as_view(),name='s'),
url(r'^star/(?P<artist>\D+)',Actorstats.as_view(),name='p'),


]
