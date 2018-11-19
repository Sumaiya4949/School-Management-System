
from django.urls import path
from .views import *
urlpatterns = [
    path('register/', registration , name ='user-registration'),
    path('login/', user_login , name ='user-login'),
    path('logout/', user_logout , name ='user-logout'),
]