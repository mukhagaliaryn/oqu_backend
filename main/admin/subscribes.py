from django.contrib import admin

from main.models import Rating, Subscribe


# Subscribes
# ----------------------------------------------------------------------------------------------------------------------
# Rating
class RatingAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'rating_score', )
    list_filter = ('course', 'user', )


# Subscribe
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'course_price', )
    list_filter = ('course', 'user', )


# ----------------------------------------------------------------------------------------------------------------------
admin.site.register(Rating, RatingAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
