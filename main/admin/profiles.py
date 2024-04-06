from django.contrib import admin
from main.models import UserCourse, UserChapter, UserLesson


class UserChapterTable(admin.TabularInline):
    model = UserChapter
    extra = 0


class UserLessonTable(admin.TabularInline):
    model = UserLesson
    extra = 0


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'is_completed', )
    list_filter = ('user', 'course', 'is_completed', )
    search_fields = ('course', 'user', )

    inlines = [UserChapterTable, UserLessonTable]


admin.site.register(UserCourse, UserCourseAdmin)
