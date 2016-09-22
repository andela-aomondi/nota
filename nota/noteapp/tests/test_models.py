from datetime import datetime

from django.test import TestCase

from .models import Note


class NoteModelTestCase(TestCase):
    def setUp(self):
        Note.objects.create(
                name='test_note_1',
                date_created=datetime.now(),
                content='Test Note 1'
        )
        Note.objects.create(
                name='test_note_2',
                date_created=datetime.now(),
                content='Test Note 2'
        )

    def test_notes_are_created_correctly(self):
        note = Note.objects.get(name="test_note_1")

        self.assertEqual(note.content, 'Test Note 1')
