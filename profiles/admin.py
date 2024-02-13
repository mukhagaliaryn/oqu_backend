from django.contrib import admin
from .models import Profile, Headliner, UserCourse, UserChapter, UserLesson


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty', 'is_author', )


class HeadlinerAdmin(admin.ModelAdmin):
    pass


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'is_completed', )
    list_filter = ('is_completed', )


class UserChapterAdmin(admin.ModelAdmin):
    list_display = ('user', 'chapter', 'is_completed', )
    list_filter = ('is_completed', )


class UserLessonAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'is_completed', )
    list_filter = ('is_completed',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Headliner, HeadlinerAdmin)
admin.site.register(UserCourse, UserCourseAdmin)
admin.site.register(UserChapter, UserChapterAdmin)
admin.site.register(UserLesson, UserLessonAdmin)
