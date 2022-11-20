from django.contrib import admin
from TODO_web_app.models import Tasklist
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','task','done']


admin.site.register(Tasklist,TaskAdmin)