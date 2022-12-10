from django.urls import path
from manager import views

urlpatterns = [
    path('home/',views.manager_home,name = "manager-home"),
    path('create_task/',views.send_interns_info,name = "create_task"),
    path('task/',views.create_task,name="task"),
    path('blockers/',views.show_blockers,name="showblockers"),
    path('send/',views.sendqueries,name="query"),
    path('solve/',views.solvequeries,name="resolve"),
    path('show/',views.show_progress,name = "progress"),
    path('info2/',views.send_interns_info_points,name = "send-interns-info"),
    path('points/',views.give_points,name = "add-points")

]