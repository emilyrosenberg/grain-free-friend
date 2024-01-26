from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe


class Option(models.Model):
    """Option model"""

    user = models.ForeignKey(
        User, related_name="option_owner", on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe, related_name="user_option", on_delete=models.CASCADE
    )

    # options = models.ManyToManyField(
    #     User, blank=True
    # )

    def __str__(self):
        return f"{self.user.username}'s {self.recipe.title} recipe"
