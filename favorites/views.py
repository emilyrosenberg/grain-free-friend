from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Option


class Favorites(LoginRequiredMixin, TemplateView):
    """View user's favorites"""

    template_name = "favorites/favorites.html"

    def get_context_data(self, **kwargs):
        option = Option.objects.filter(user=self.request.user)
        # Add code for more filters here

        context = {"option": option}

        return context
