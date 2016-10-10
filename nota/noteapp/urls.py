"""Imports for nota urls."""
from django.conf.urls import url

from noteapp.views import HomePageView, NoteDetailView


urlpatterns = [
    url(r'^$', HomePageView.as_view()),
    url(r'^notes/$', NoteDetailView.as_view())
]
