from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import (
    Category, Topic, Language, Course, Purpose, Chapter, Lesson, Video, Article, Rating
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


# Product admin
# ---------------------------------------------------------------------------------------
class PurposeTable(admin.TabularInline):
    model = Purpose
    fields = ('product', 'item',)
    extra = 1


class ChapterTable(admin.TabularInline):
    model = Chapter
    fields = ('product', 'chapter_name', 'about', )
    extra = 1


class CourseAdmin(SummernoteModelAdmin):
    list_display = ('name', 'category', 'topic', 'last_update', 'is_headline', )
    list_filter = ('category', 'topic',)
    filter_horizontal = ('authors', 'requirements', 'ln', )
    summernote_fields = ('description', )

    inlines = [PurposeTable, ChapterTable, ]


# Lesson admin
# ------------------------------------------------------------------------------
class VideoTabular(admin.TabularInline):
    model = Video
    extra = 1


class ArticleTabular(SummernoteModelAdminMixin, admin.TabularInline):
    model = Article
    extra = 1
    summernote_fields = ('description', )


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'duration', 'date_created', 'access', )
    search_fields = ('title', 'chapter')
    list_filter = ('access', 'chapter', 'lesson_type', )

    inlines = (VideoTabular, ArticleTabular, )


class RatingAdmin(admin.ModelAdmin):
    pass


# ------------------------------------------------------------------------------
admin.site.register(Category, CategoryAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Rating, RatingAdmin)
