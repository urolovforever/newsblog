from django.urls import path

from .views import *

urlpatterns = [
    path('',SignUp.as_view(), name = 'signup'),
    path('logout',user_logout, name = 'logout')
]