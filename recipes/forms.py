from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """Form to create a recipe"""

    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
            "image_alt",
            "level",
            "method",
        ]

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        # Overrides label names, the one on the right is the display title
        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Ingredients",
            "instructions": "Instructions",
            "image": "Image",
            "image_alt": "Image description",
            "level": "Level",
            "method": "Method",
        }
