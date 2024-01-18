from django.contrib import admin
from .models import Recipe


# From tutorial, customize this later
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "meal_type",
        "instructions",
        "ingredients",
        "image",
    )
    # Filter by meal types on the admin panel
    list_filter = ("meal_type",)
