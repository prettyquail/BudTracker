from django.urls import path
from core import views

urlpatterns = [
    path("",views.Login,name="login"),
    path("register/",views.Register,name="register"),
    path("logout/",views.Logout,name="logout"),
]