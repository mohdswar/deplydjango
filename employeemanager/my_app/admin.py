from django.contrib import admin
from .models import Employee, Task,Role

admin.site.register(Employee)

admin.site.register(Task)
admin.site.register(Role)