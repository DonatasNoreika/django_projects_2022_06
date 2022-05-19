from django.contrib import admin

# Register your models here.
from .models import (Project,
                     Client,
                     Employee,
                     Invoice,
                     Job)

class JobInline(admin.TabularInline):
    model = Job
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'client', 'manager')
    inlines = [JobInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Invoice)
admin.site.register(Job)
