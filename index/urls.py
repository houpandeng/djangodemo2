from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from index.views import *
urlpatterns = [
    path('index/', index_views),
    path('01-temp/', temp_views),
    path('02-temp/', temp2_views),
    path('03-var/', var_views),
    path('04-test/', test_views111),
    path('05-add/', add_views, name='add'),
    path('06-queryall/', queryall ),
]

urlpatterns += [

    path('07-queryall/',queryall_views,name='queryall'),
    url(r'^08-update/(\d{1,})/$', update_views,name='update'),


]


