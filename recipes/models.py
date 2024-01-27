""" The recipes app was inspired by the app of the same name in the Django Recipe Sharing tutorial by Dee Mc. This functionality is based on the tutorial. """

from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


# Choice Fields
LEVEL = (("easy", "Easy"), ("moderate", "Moderate"), ("fancy", "Fancy"))

METHOD = (("stovetop", "Stovetop"), ("oven", "Oven"), ("microwave", "Microwave"))

TAG1 = (
    ("keto", "Keto"),
    ("vegan", "Vegan"),
    ("gluten-free", "Gluten-free"),
    ("parve", "Parve"),
    ("nut-free", "Nut-free"),
    ("dairy-free", "Dairy-free"),
)

TAG2 = (
    ("keto", "Keto"),
    ("vegan", "Vegan"),
    ("gluten-free", "Gluten-free"),
    ("parve", "Parve"),
    ("nut-free", "Nut-free"),
    ("dairy-free", "Dairy-free"),
    ("--", "--"),
)

TAG3 = (
    ("keto", "Keto"),
    ("vegan", "Vegan"),
    ("gluten-free", "Gluten-free"),
    ("parve", "Parve"),
    ("nut-free", "Nut-free"),
    ("dairy-free", "Dairy-free"),
    ("--", "--"),
)


class Recipe(models.Model):
    """
    A model to create and manage recipes
    """

    user = models.ForeignKey(
        User, related_name="recipe_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False)
    # If file is larger, it will scale to the right size and upload to Cloudinary
    image = ResizedImageField(
        # Crop to a square https://stackoverflow.com/questions/71709173/fetch-image-and-crop-before-save-django
        size=[400, 400],
        crop=["middle", "center"],
        quality=75,
        upload_to="recipes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    # dropdown menus
    level = models.CharField(max_length=50, choices=LEVEL, default="easy")
    method = models.CharField(max_length=50, choices=METHOD, default="stovetop")
    tag1 = models.CharField(max_length=50, choices=TAG1, default="gluten-free")
    tag2 = models.CharField(max_length=50, choices=TAG2, default="--")
    tag3 = models.CharField(max_length=50, choices=TAG3, default="--")

    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)
