from modeltranslation.translator import translator, TranslationOptions
from src.platform.myaccount.models import Account


class AccountTranslationOptions(TranslationOptions):
    fields = ('specialty', 'bio', )


translator.register(Account, AccountTranslationOptions)
