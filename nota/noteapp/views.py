"""Imports for nota views."""
from django.contrib.auth.models import User
from django.views.generic import TemplateView

from .models import Note


class HomePageView(TemplateView):
    """View to serve the main template."""

    template_name = "index.html"


class NoteDetailView(TemplateView):
    """View to handle listing notes."""

    # def get_context_data(self, **kwargs):
    #     context = super(HomePageView, self).get_context_data(**kwargs)
    #
    #     context['notes'] = Note.objects.all()
    #
    #     return context


class NoteCreateView():
    """View to handle creating notes."""

    pass


class NoteEditView():
    """View to handle editing notes."""

    pass


class NoteDeleteView():
    """View to handle deleting notes."""

    pass
