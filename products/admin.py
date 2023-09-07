from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin

from .models import Category, Topic, Product, Purpose, Feature, Chapter, Lesson, Video, Task, Question, Answer


class TopicInline(admin.TabularInline):
    model = Topic
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', )
    exclude = ('category', )
    inlines = (TopicInline, )


# Product admin
# ---------------------------------------------------------------------------------------
class PurposeTable(SummernoteModelAdminMixin, admin.StackedInline):
    model = Purpose
    fields = ('product', 'item',)
    extra = 1
    summernote_fields = ('item',)


class FeaturesTable(admin.TabularInline):
    model = Feature
    fields = ('product', 'label', 'item', )
    extra = 1


class ChapterTable(admin.TabularInline):
    model = Chapter
    fields = ('product', 'chapter_name', 'about', )
    extra = 1


class ProductAdmin(SummernoteModelAdmin):
    list_display = ('name', 'product_type', 'class_level', )
    list_filter = ('class_level', 'product_type', )
    filter_horizontal = ('authors',)
    summernote_fields = ('about', 'description', )

    inlines = [PurposeTable, FeaturesTable, ChapterTable, ]


# Lesson admin
# ------------------------------------------------------------------------------
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'access', 'date_created', )
    search_fields = ('title', 'chapter')
    list_filter = ('access', )


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'duration', )


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'duration', )


class AnswerTable(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'format', 'quiz', )

    inlines = [AnswerTable, ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Question, QuestionAdmin)
