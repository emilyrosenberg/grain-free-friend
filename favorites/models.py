from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe


class Favorite(models.Model):
    """ Favorite model """
    user = models.ForeignKey(
        User, related_name="favorite_owner", on_delete=models.CASCADE
        )
    recipe = models.ForeignKey(
        Recipe, related_name="user_favorite", on_delete=models.CASCADE
        )
    level = models.CharField(max_length=50)
    method = models.CharField(max_length=50)

    def __str__(self):
        return (
            f"{self.user.username}'s {self.recipe.level} {self.recipe.method} meal"
        )