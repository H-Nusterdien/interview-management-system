from django import forms
from notes_management import models


class CreateNoteForm(forms.ModelForm):
    """
    Form for creating a new note associated with a candidate.

    Uses Django's ModelForm to create a form based on the Note model.

    Fields:
    - title: CharField for the title of the note.
    - description: TextField for the description/content of the note.
    """
    class Meta:
        model = models.Note
        fields = ['title', 'description']


class UpdateNoteForm(forms.ModelForm):
    """
    Form for updating an existing note associated with a candidate.

    Uses Django's ModelForm to create a form based on the Note model.

    Fields:
    - user: ForeignKey to User model representing the user who created the note.
    - title: CharField for the title of the note.
    - description: TextField for the description/content of the note.
    """
    class Meta:
        model = models.Note
        fields = ['user', 'title', 'description']
