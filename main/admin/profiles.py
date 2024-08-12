from django.contrib import admin
from main.models import OldUserCourse, OldUserChapter, OldUserLesson


class OldUserChapterTable(admin.TabularInline):
    model = OldUserChapter
    extra = 0


class OldUserLessonTable(admin.TabularInline):
    model = OldUserLesson
    extra = 0


class OldUserCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'is_completed', )
    list_filter = ('user', 'course', 'is_completed', )
    search_fields = ('course', 'user', )

    inlines = [OldUserChapterTable, OldUserLessonTable]


admin.site.register(OldUserCourse, OldUserCourseAdmin)
