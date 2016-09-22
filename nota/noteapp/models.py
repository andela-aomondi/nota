"""Nota Models."""
from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    """Note model.

    Defines:
        Name -  The name of the note
        Date_created -  The date and time the note was created
        Content - Of course, the actual content of the note
    """

    content = models.TextField(null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(null=True)
    owner = models.ForeignKey(User, null=False, default=1)

    def __unicode__(self):
        return self.name

    def get_owner(self):
        return self.owner.first_name + self.owner.last_name
