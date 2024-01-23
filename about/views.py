from django.views.generic import ListView
from recipes.models import Recipe


class About(ListView):
    template_name = 'templates/about.html'
    model = Recipe
    context_object_name = 'recipes'