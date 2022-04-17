from atexit import register
from django.urls import path
from . import views as userViews

urlpatterns = [
    path('', userViews.index , name="user-home" ),
    path('register', userViews.register , name="user-register" ),
    path('login', userViews.login , name="user-login" ),
    path('logout', userViews.logout , name="user-logout" ),
    path('success', userViews.success , name="user-redirect" ),
]