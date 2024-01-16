from django.views.generic import CreateView, ListView

# This mixin makes sure that only logged in users can create a recipe
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm


class Recipes(ListView):
    """ View all recipes """
    template_name = 'recipes/recipes.html'
    model = Recipe
    # Accesses properties of objects in the backend
    context_object_name = 'recipes'
    

class AddRecipe(LoginRequiredMixin, CreateView):
    """ Add recipe view """
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'

    # 
    def form_valid(self, form):
        # Update form's instance of the user and set it to the person who is creating the recipe (the logged in user)
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)