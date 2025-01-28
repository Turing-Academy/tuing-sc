from django.contrib import admin
from .models import *

class LessonScheduleInline(admin.TabularInline):
    model = LessonSchedule
    extra = 1

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [LessonScheduleInline]

admin.site.register(Classroom)
admin.site.register(RecordLink)