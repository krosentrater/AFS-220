from django.urls import path
from . import views


urlpatterns = [
    path('', views.attractions, name="attractions"),
]