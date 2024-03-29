""" The recipes app was inspired by the app of the same name in the Django Recipe Sharing tutorial by Dee Mc. These forms are based on the tutorial. """

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
            "tag1",
            "tag2",
            "tag3",
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
            "tag1": "Tag 1",
            "tag2": "Tag 2",
            "tag3": "Tag 3",
        }
