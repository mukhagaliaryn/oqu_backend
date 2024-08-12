from modeltranslation.translator import register, TranslationOptions
from .models import OldCategory, OldSubCategory


@register(OldCategory)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(OldSubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

