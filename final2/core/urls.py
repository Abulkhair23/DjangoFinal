from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = [
    path('books/', BookViewSet),
    path('journals/', JournalViewSet)
]
