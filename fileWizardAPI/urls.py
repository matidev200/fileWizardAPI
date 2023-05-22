from django.urls import path, include
from api import views

urlpatterns = [
    path('api/hello_world', views.hello_world, name='test' ),
]
