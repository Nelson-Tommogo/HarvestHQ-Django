from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="harvesthqapp-home"),
        path("harvesthqapp/", views.about, name="harvesthqapp-about"),
]