from django.urls import path
from .views import *

urlpatterns = [
  	path('', cal, name='login'),
    ]