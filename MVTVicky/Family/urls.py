from django.urls import path
from Family.views import home_page
from Family.views import Search


urlpatterns = [
path("", home_page, name= "home_page"),
path("find/", Search, name="Search"),    
]
