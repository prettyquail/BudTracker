from django.urls import path
from manager import views

urlpatterns = [
    path('home/',views.manager_home,name = "manager-home"),
    path('create_task/',views.send_interns_info,name = "create_task"),
    path('task/',views.create_task,name="task"),
    path('blockers/',views.show_blockers,name="showblockers"),
    path('send/',views.sendqueries,name="query"),
    path('solve/',views.solvequeries,name="resolve"),
]