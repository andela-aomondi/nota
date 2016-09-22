from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'content')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Note, NoteAdmin)
