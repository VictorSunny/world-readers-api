from django.urls import path
from . import views



urlpatterns = [
    path('', views.UserCreationView.as_view(), name= 'signup'),
]