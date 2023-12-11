from django import forms
from notes_management import models


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['title', 'description']


class UpdateNoteForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['user', 'title', 'description']
