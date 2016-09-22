"""Imports for nota urls."""
from django.conf.urls import url

from noteapp.views import HomePageView


urlpatterns = [
    url(r'^$', HomePageView.as_view())
]
