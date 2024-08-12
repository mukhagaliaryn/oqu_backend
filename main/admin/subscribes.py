from django.contrib import admin

from main.models import OldRating, OldSubscribe


# Subscribes
# ----------------------------------------------------------------------------------------------------------------------
# Rating
class OldRatingAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'rating_score', )
    list_filter = ('course', 'user', )


# Subscribe
class OldSubscribeAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'course_price', )
    list_filter = ('course', 'user', )


# ----------------------------------------------------------------------------------------------------------------------
admin.site.register(OldRating, OldRatingAdmin)
admin.site.register(OldSubscribe, OldSubscribeAdmin)
