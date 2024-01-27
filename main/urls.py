""" This web app was inspired by the Django Recipe Sharing tutorial by Dee Mc. The functionality here is based on the tutorial. """

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("djrichtextfield/", include("djrichtextfield.urls")),
    # finds the urls file within the home app
    path("", include("home.urls")),
    path("about/", include("about.urls")),
    path("recipes/", include("recipes.urls")),
    path("favorites/", include("favorites.urls")),
]
