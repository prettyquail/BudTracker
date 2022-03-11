from django.urls import path
from intern import views

urlpatterns = [
    path('home/',views.manager_home,name = "manager-home"),
]