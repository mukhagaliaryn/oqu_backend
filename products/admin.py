from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import (
    Category, Topic, Language, Course, Purpose, Chapter, Lesson, Video, Article, Rating, Subscribe
)


# Category admin
# ------------------------------------------------------------------------------------------------
class TopicInline(TranslationTabularInline):
    model = Topic
    extra = 1


class LanguageAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', )
    exclude = ('category', )
    inlines = (TopicInline, )


# Course admin
# ----------------------------------------------------------------------------------------------------------------------
class PurposeTable(admin.TabularInline):
    model = Purpose
    fields = ('product', 'item',)
    extra = 0


class ChapterTable(admin.TabularInline):
    model = Chapter
    fields = ('product', 'chapter_index', 'chapter_name', )
    extra = 0


class CourseAdmin(SummernoteModelAdmin):
    list_display = ('name', 'category', 'topic', 'last_update', 'course_type', )
    list_filter = ('category', 'topic', 'course_type',)
    search_fields = ('name', 'category', 'topic',)
    filter_horizontal = ('authors', 'requirements', 'ln', )
    summernote_fields = ('description', )

    inlines = [PurposeTable, ChapterTable, ]


class RatingAdmin(admin.ModelAdmin):
    pass


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'course_price', )
    list_filter = ('course', 'user', )


# Lesson admin
# ----------------------------------------------------------------------------------------------------------------------
class VideoTabular(admin.TabularInline):
    model = Video
    extra = 0


class ArticleTabular(SummernoteModelAdminMixin, admin.TabularInline):
    model = Article
    extra = 0
    summernote_fields = ('description', )


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'duration', 'index', 'date_created', 'access', )
    search_fields = ('title', 'chapter')
    list_filter = ('access', 'chapter', 'lesson_type', )

    inlines = (VideoTabular, ArticleTabular, )


# ----------------------------------------------------------------------------------------------------------------------
admin.site.register(Category, CategoryAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
