from django.contrib import admin

# Register your models here.

from .models import Course, Lection, Homework


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Course, CourseAdmin)


class LectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'presentation']
    list_editable = ['presentation']


admin.site.register(Lection, LectionAdmin)


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['txt', 'comment', 'mark']
    list_editable = ['comment', 'mark']


admin.site.register(Homework, HomeworkAdmin)
