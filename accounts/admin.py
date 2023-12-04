from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Account
from django.contrib.auth.models import Group


# User Admin
# -----------------------------------------------------------------------------------------------
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'full_name', 'user_type', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser', 'user_type', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональные данные', {'fields': ('full_name', 'user_type', 'image', 'last_login',)}),
        ('Разрешения', {'fields': ('is_superuser', 'is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'full_name', 'user_type', )
    ordering = ('email',)
    filter_horizontal = ()


# Account admin
# -----------------------------------------------------------------------------------------------
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'account_fill',)
    list_filter = ('account_fill',)

    search_fields = ('user', 'city', )
    ordering = ('user',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)

admin.site.unregister(Group)
