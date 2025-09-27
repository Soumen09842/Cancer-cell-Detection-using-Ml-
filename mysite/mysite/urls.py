
from django.contrib import admin
from django.urls import path
import myapp.views
urlpatterns = [
    path("", myapp.views.home),
    path("about-us/", myapp.views.about),
    path("analysis/", myapp.views.analysis),
    path("team/", myapp.views.team),
    path("contact/", myapp.views.contact),
    path("pred/",myapp.views.pred)
]
