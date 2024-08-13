from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from src.platform.myaccount.models import Account


class AccountAdmin(TranslationAdmin):
    list_display = ('user', 'account_type', 'specialty', 'account_fill', )
    list_filter = ('account_type', )


admin.site.register(Account, AccountAdmin)
