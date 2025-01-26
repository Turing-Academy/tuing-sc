from django.contrib import admin
from .models import *

class TeacherImageInline(admin.TabularInline):
    model = TeacherImage
    extra = 1

class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 1
    inlines = [TeacherImageInline]

class LessonScheduleInline(admin.TabularInline):
    model = LessonSchedule
    extra = 1

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [TeacherInline, LessonScheduleInline]

admin.site.register(Classroom)