from django.urls import path
from .views import Favorites, GetOption, AddOption


urlpatterns = [
    path("", Favorites.as_view(), name="favorites"),
    path("favorite_finder/", GetOption.as_view(), name="favorite_finder"),
    # path("add_option/<int:pk>/", AddOption.as_view(), name="add_option"),
    path("favorites/add_option/<int:pk>/", AddOption.as_view(), name="add_option"),
]
