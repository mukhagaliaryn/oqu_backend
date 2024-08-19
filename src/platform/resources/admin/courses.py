from django.contrib import admin
from django_summernote.admin import SummernoteModelAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from src.platform.resources.models import Subcategory, Purpose, Chapter, Lesson, Category, Course, Video


# Category
# ----------------------------------------------------------------------------------------------------------------------
class SubCategoryInline(TranslationTabularInline):
    model = Subcategory
    extra = 1
    prepopulated_fields = {'slug': ('name_en', )}


class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name_en', )}
    inlines = (SubCategoryInline, )


# Course
# ----------------------------------------------------------------------------------------------------------------------
# Purpose Tab
class PurposeTable(TranslationTabularInline):
    model = Purpose
    extra = 0


# Chapter Tab
class ChapterTable(TranslationTabularInline):
    model = Chapter
    extra = 0


# Video
class LessonTable(TranslationTabularInline):
    model = Lesson
    extra = 0


# Video
class OldVideoTable(admin.TabularInline):
    model = Video
    extra = 0


# Course
class CourseAdmin(SummernoteModelAdminMixin, TranslationAdmin):
    list_display = ('name', 'category', 'sub_category', 'course_type', 'last_update', )
    list_filter = ('category', 'sub_category', 'course_type',)
    search_fields = ('name', 'category', 'sub_category', )
    filter_horizontal = ('authors', 'ln', )
    summernote_fields = ('description', )
    inlines = (PurposeTable, ChapterTable, LessonTable, OldVideoTable, )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
