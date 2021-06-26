from django.contrib import admin

from .models import Profile, Card, Category


admin.site.register(Card)
admin.site.register(Profile)
admin.site.register(Category)

