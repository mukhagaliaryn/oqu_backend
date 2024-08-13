from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from main.models import CloneUser, CloneAccount


class CloneUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'full_name', 'is_staff', 'is_active', 'is_superuser', )
    list_filter = ('is_active', 'is_staff', )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal data'), {'fields': ('full_name', 'image', 'birthday', 'last_login',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', )}),
    )
    filter_horizontal = ()


# Account Admin
# ----------------------------------------------------------------------------------------------------------------------
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_type', 'id_number', 'specialty', )
    list_filter = ('account_type',)

    fieldsets = (
        (None, {'fields': ('user', 'account_type', 'id_number', 'specialty', )}),
        (_('Personal data'), {'fields': ('city', 'address', 'phone', 'website', )}),
    )

    search_fields = ('user__full_name', 'user__email', 'id_number', 'specialty', )
    ordering = ('user',)
    filter_horizontal = ()


admin.site.register(CloneUser, CloneUserAdmin)
admin.site.register(CloneAccount, AccountAdmin)
