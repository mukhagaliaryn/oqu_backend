from django.contrib import admin
from src.platform.myaccount.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_type', 'specialty', 'account_fill', )
    list_filter = ('account_type', )


admin.site.register(Account, AccountAdmin)
