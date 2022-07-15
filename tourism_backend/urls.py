from django.urls import path
from .views import *

urlpatterns = [
    path('application/', APIApplication.as_view()),
]