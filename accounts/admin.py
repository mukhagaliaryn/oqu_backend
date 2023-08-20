from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Account, Institution, Language, ClassGroup
from django.contrib.auth.models import Group


# User Admin
# -----------------------------------------------------------------------------------------------
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser', 'user_type', )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Персональные данные', {'fields': ('first_name', 'last_name', 'user_type', 'image', 'last_login',)}),
        ('Разрешения', {'fields': ('is_superuser', 'is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name', 'user_type', )
    ordering = ('username',)
    filter_horizontal = ()


# Account admin
# -----------------------------------------------------------------------------------------------
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'account_fill',)
    list_filter = ('account_fill',)

    search_fields = ('user', 'city', )
    ordering = ('user',)
    filter_horizontal = ()


# Institution admin
# ------------------------------------------------------------------------------------------------
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'inst_type', 'ownership', 'school_view', 'slope', 'owner',)
    filter_horizontal = ('ln', )
    list_filter = ('inst_type', 'ownership', 'school_view', 'slope',)
    search_fields = ('name', )


# ClassGroup admin
# ------------------------------------------------------------------------------------------------
class ClassGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_level', 'institution', 'teacher', )
    list_filter = ('class_level', 'institution',)
    search_fields = ('name', )
    filter_horizontal = ('students', 'subjects', )


admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(ClassGroup, ClassGroupAdmin)
admin.site.register(Language)

admin.site.unregister(Group)
