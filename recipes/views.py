from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.db.models import Q

# This mixin makes sure that only logged in users can create a recipe
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm


class Recipes(ListView):
    """View all recipes"""

    template_name = "recipes/recipes.html"
    model = Recipe
    # Accesses properties of objects in the backend
    context_object_name = "recipes"

    # Searches for keywords within the recipes
    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes


class RecipeDetail(DetailView):
    """View a single recipe"""

    template_name = "recipes/recipe_detail.html"
    model = Recipe
    # Accesses properties of objects in the backend
    context_object_name = "recipe"


class AddRecipe(LoginRequiredMixin, CreateView):
    """Add recipe view"""

    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    #
    def form_valid(self, form):
        # Update form's instance of the user and set it to the person who is creating the recipe (the logged in user)
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit a recipe """
    template_name = 'recipes/edit_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'

    def test_func(self):
        return self.request.user == self.get_object().user


# These mixins make sure only the logged in user can delete their recipes
class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a recipe """
    model = Recipe
    success_url = '/recipes/'

    def test_func(self):
        return self.request.user == self.get_object().user