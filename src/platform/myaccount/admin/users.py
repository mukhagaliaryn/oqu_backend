from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from src.platform.myaccount.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'full_name', 'is_staff', 'is_active', 'is_superuser', )
    list_filter = ('is_active', 'is_staff', )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal data'), {'fields': ('full_name', 'image', 'birthday', 'last_login',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', )}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide", ),
                "fields": ("email", "username", 'full_name', 'password1', 'password2', ),
            },
        ),
    )
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
