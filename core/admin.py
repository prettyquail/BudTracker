from django.contrib import admin
from core.models import Account,Task,Blocker,Progress,Blocker_Answer,LoginLogoutLog
# Register your models here.
admin.site.register(Account)
admin.site.register(Task)
admin.site.register(Blocker)
admin.site.register(Progress)
admin.site.register(Blocker_Answer)
admin.site.register(LoginLogoutLog)
