from django.urls import path
from .views import Favorites, GetOption


urlpatterns = [
    path("", Favorites.as_view(), name="favorites"),
    path("favorite_finder/", GetOption.as_view(), name="favorite_finder"),
]
