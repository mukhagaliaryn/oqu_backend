from django.contrib import admin
from .models import Profile, Headliner


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty', 'is_author', )


class HeadlinerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Headliner, HeadlinerAdmin)
