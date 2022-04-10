
from typing import List
from django import urls
from django.contrib import admin
from django.urls import path, include
from MVTVicky.views import Family, Members_List


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Members_List/', Members_List),
    path("Family/", include("Family.urls")),
]
