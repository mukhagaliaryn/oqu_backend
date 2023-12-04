from django.contrib import admin
from centres.models import Institution, ClassGroup, Direction


# Institution admin
# ------------------------------------------------------------------------------------------------
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction', 'date_created', 'owner',)
    list_filter = ('direction', )
    search_fields = ('name', 'direction', )
    fieldsets = (
        (None, {'fields': ('image', 'name', 'direction', )}),
        ('Контакты', {'fields': ('date_created', 'phone', 'email', 'website', 'address', 'owner', )}),
    )


# ClassGroup admin
# ------------------------------------------------------------------------------------------------
class ClassGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'flow', 'institution', 'teacher', )
    list_filter = ('flow', 'institution',)
    search_fields = ('name', )

    fieldsets = (
        (None, {'fields': ('name', 'institution', 'teacher', 'flow')}),
        ('Участники и программы', {'fields': ('students', 'subjects', )}),
    )
    filter_horizontal = ('students', 'subjects', )


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(ClassGroup, ClassGroupAdmin)
admin.site.register(Direction)
