from django.contrib import admin
from django.urls import path,include
from index.views import *
urlpatterns = [
    path('admin/', admin.site.urls),





]
