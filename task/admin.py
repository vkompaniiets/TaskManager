from django.contrib import admin

from task.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('assignee', 'created_by', 'name', 'completed')
    raw_id_fields = ('assignee', )
    list_per_page = 50

admin.site.register(Task, TaskAdmin)