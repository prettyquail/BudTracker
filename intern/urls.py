from django.urls import path
from intern import views

urlpatterns = [
    path('home/',views.intern_home,name = "intern-home"),
]