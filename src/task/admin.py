from django.contrib import admin

from task.models import Attachment, Task, TaskList


admin.site.register(TaskList)
admin.site.register(Attachment)
admin.site.register(Task)
