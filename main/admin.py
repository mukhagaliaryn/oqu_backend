from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import (
    Category, SubCategory, Course, Purpose, Chapter, Lesson, Video, Article, Rating, Subscribe
)


# Category
# ----------------------------------------------------------------------------------------------------------------------
class SubCategoryInline(TranslationTabularInline):
    model = SubCategory
    extra = 1


class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', )
    exclude = ('category', )
    inlines = (SubCategoryInline, )


# Course admin
# ----------------------------------------------------------------------------------------------------------------------
# Purpose Tab
class PurposeTable(admin.TabularInline):
    model = Purpose
    fields = ('course', 'item', )
    extra = 0


# Chapter Tab
class ChapterTable(admin.TabularInline):
    model = Chapter
    extra = 0


# Video
class LessonTable(admin.TabularInline):

    model = Lesson
    extra = 0


# Video
class VideoTable(admin.TabularInline):
    model = Video
    extra = 0


# Article
class ArticleTable(SummernoteModelAdminMixin, admin.TabularInline):
    model = Article
    extra = 0
    summernote_fields = ('description', )


# Course
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('name', 'category', 'sub_category', 'last_update', 'course_type', )
    list_filter = ('category', 'sub_category', 'course_type',)
    search_fields = ('name', 'category', 'sub_category', )
    filter_horizontal = ('course_authors', 'ln', )
    summernote_fields = ('description', )

    inlines = [PurposeTable, ChapterTable, LessonTable, VideoTable, ArticleTable, ]


# Subscribes
# ----------------------------------------------------------------------------------------------------------------------
# Rating
class RatingAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'rating_score', )
    list_filter = ('course', 'user', )


# Subscribe
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'course_price', )
    list_filter = ('course', 'user', )


# ----------------------------------------------------------------------------------------------------------------------
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
