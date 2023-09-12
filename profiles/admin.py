from django.contrib import admin
from .models import Profile, UserQuizData, UserAnswer, UserChapter, UserLesson, UserProduct, UserVideo, UserTask


# UserProductAdmin
class UserProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'score', 'is_subscribe', )


# UserChapterAdmin
class UserChapterAdmin(admin.ModelAdmin):
    list_display = ('user', 'chapter', 'score', 'is_done', )


# UserChapterAdmin
class UserLessonAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'score', 'is_done', )


class UserVideoAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'score', 'is_done', )


class UserTaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'score', 'is_done', )


class UserQuizDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'finish_time', 'status', )
    list_filter = ('status', )
    filter_horizontal = ('questions', )


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_quiz', 'score', 'max_score', )


admin.site.register(Profile)

admin.site.register(UserProduct, UserProductAdmin)
admin.site.register(UserChapter, UserChapterAdmin)
admin.site.register(UserLesson, UserLessonAdmin)

admin.site.register(UserVideo, UserVideoAdmin)
admin.site.register(UserTask, UserTaskAdmin)
admin.site.register(UserQuizData, UserQuizDataAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)

