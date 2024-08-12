from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, OldAccount
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


class CloneUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'full_name', 'is_staff', 'is_active', 'is_superuser', )
    list_filter = ('is_active', 'is_staff', )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal data'), {'fields': ('full_name', 'image', 'birthday', 'last_login',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', )}),
    )
    filter_horizontal = ()


# -----------------------------------------------------------------------------------------------
admin.site.register(User, UserAdmin)
admin.site.register(OldAccount, AccountAdmin)
# admin.site.register(CloneUser, CloneUserAdmin)

admin.site.unregister(Group)
