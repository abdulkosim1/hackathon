from django.contrib import admin
from feedback.models import Like, Comment, Favorite, Rating


admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Rating)
