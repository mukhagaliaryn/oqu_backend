from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Topic


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


class TopicTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(Category, CategoryTranslationOptions)
translator.register(Topic, TopicTranslationOptions)
