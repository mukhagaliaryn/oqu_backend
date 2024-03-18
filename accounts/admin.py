from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Account
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


# User Admin
# ----------------------------------------------------------------------------------------------------------------------
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'full_name', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal data'), {'fields': ('full_name', 'image', 'gender', 'birthday', 'last_login',)}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'full_name', )
    ordering = ('email',)
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


# -----------------------------------------------------------------------------------------------
admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)

admin.site.unregister(Group)
