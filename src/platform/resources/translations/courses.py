from modeltranslation.translator import translator, TranslationOptions
from src.platform.resources.models import Category, Subcategory, Course, Purpose, Chapter, Lesson


# Category
# ----------------------------------------------------------------------------------------------------------------------
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


class SubcategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


# Course
# ----------------------------------------------------------------------------------------------------------------------
class CourseTranslationOptions(TranslationOptions):
    fields = ('name', 'about', 'description', )


class PurposeTranslationOptions(TranslationOptions):
    fields = ('item', )


class ChapterTranslationOptions(TranslationOptions):
    fields = ('name', )


class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'about', )


translator.register(Category, CategoryTranslationOptions)
translator.register(Subcategory, SubcategoryTranslationOptions)
translator.register(Course, CourseTranslationOptions)
translator.register(Purpose, PurposeTranslationOptions)
translator.register(Chapter, ChapterTranslationOptions)
translator.register(Lesson, LessonTranslationOptions)
