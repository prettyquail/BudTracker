from django.urls import path
from intern import views

urlpatterns = [
    path('home/',views.intern_home,name = "intern-home"),
    path('info/',views.progress_info,name = "progress-info"),
    path('progress/',views.update_progress,name = "add-progress"),
    path('info2/',views.send_managers_info,name = "send-managers-info"),
    path('blocker/',views.addblocker,name = "add-blocker"),
    path('show-blocker/',views.trackblockers,name = "show-blockers"),
]