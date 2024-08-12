from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from main.models import *


# Category
# ----------------------------------------------------------------------------------------------------------------------
class OldSubCategoryInline(TranslationTabularInline):
    model = OldSubCategory
    extra = 1


class OldCategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', )
    exclude = ('category', )
    inlines = (OldSubCategoryInline, )


# Course admin
# ----------------------------------------------------------------------------------------------------------------------
# Purpose Tab
class OldPurposeTable(admin.TabularInline):
    model = OldPurpose
    fields = ('course', 'item', )
    extra = 0


# Chapter Tab
class OldChapterTable(admin.TabularInline):
    model = OldChapter
    extra = 0


# Video
class OldLessonTable(admin.TabularInline):

    model = OldLesson
    extra = 0


# Video
class OldVideoTable(admin.TabularInline):
    model = OldVideo
    extra = 0


# Article
class OldArticleTable(SummernoteModelAdminMixin, admin.TabularInline):
    model = OldArticle
    extra = 0
    summernote_fields = ('description', )


# Course
class OldCourseAdmin(SummernoteModelAdmin):
    list_display = ('name', 'category', 'sub_category', 'last_update', 'course_type', )
    list_filter = ('category', 'sub_category', 'course_type',)
    search_fields = ('name', 'category', 'sub_category', )
    filter_horizontal = ('course_authors', 'ln', )
    summernote_fields = ('description', )

    inlines = [OldPurposeTable, OldChapterTable, OldLessonTable, OldVideoTable, OldArticleTable, ]


# ----------------------------------------------------------------------------------------------------------------------
admin.site.register(OldCategory, OldCategoryAdmin)
admin.site.register(OldCourse, OldCourseAdmin)
