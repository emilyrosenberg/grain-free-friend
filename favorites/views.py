from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .models import Option
from recipes.models import Recipe
import random

# Views inspired by and modified from https://www.youtube.com/playlist?list=PLXuTq6OsqZjYSa-lrjd5wMGl23zpnhvln


class Favorites(TemplateView):
    """View user's favorites"""

    template_name = "favorites/favorites.html"

    def get_context_data(self):
        options = Option.objects.filter(user=self.request.user)

        context = {"options": options}

        return context

class GetOption(LoginRequiredMixin, TemplateView):
    """Get option based on search queries or empty input"""

    template_name = "favorites/favorite_finder.html"

    def get_context_data(self):
        query = self.request.GET.get("search")

        if query:
            recipes = Recipe.objects.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(ingredients__icontains=query)
                | Q(instructions__icontains=query)
                | Q(tag1__icontains=query)
                | Q(tag2__icontains=query)
                | Q(tag3__icontains=query)
            )
        else:
            if len(Recipe.objects.all()) < 1:
                recipes = []
            else:
                recipes = Recipe.objects.filter()
        # Returns a random recipe or if there are no recipes in the database, returns empty
        if len(recipes) > 0:
            recipe = random.choice(recipes)
            context = {"recipe": recipe}
        else:
            context = {}

        return context
    
    
class AddOption(View):
    def post(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        option, created = Option.objects.get_or_create(
            user=request.user,
            recipe=recipe,
        )

        # from https://docs.djangoproject.com/en/5.0/ref/models/instances/
        if not created:
            option.save()

        return HttpResponseRedirect(reverse("favorites"))
