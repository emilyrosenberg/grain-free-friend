""" The home app was inspired by the app of the same name in the Django Recipe Sharing tutorial by Dee Mc. The functionality here is based on the tutorial. """

from django.urls import path
from .views import Index


urlpatterns = [path("", Index.as_view(), name="home")]
