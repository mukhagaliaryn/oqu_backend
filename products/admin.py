from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
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
    filter_horizontal = ('authors', 'requirements', )
    summernote_fields = ('description', )

    inlines = [PurposeTable, ChapterTable, ]


# Lesson admin
# ------------------------------------------------------------------------------
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'access', 'date_created', )
    search_fields = ('title', 'chapter')
    list_filter = ('access', )


class VideoAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'duration', )


class ArticleAdmin(admin.ModelAdmin):
    pass


class RatingAdmin(admin.ModelAdmin):
    pass


# ------------------------------------------------------------------------------
admin.site.register(Category, CategoryAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Rating, RatingAdmin)
