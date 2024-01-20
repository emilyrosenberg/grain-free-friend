from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_filter = (['posted_date'])

    list_display = (
        "title",
        "instructions",
        "ingredients",
        "image",
    )
