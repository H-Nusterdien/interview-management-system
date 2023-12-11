from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from notes_management import forms as notes_management_forms
from notes_management import models as notes_management_models

from candidate_management import models as candidate_management_models


# Global context used across different views
BASE_CONTEXT = {
    'urls': {
        'sign_up': settings.SIGN_UP_URL,
        'login': settings.LOGIN_URL,
        'logout': settings.LOGOUT_URL,
    },
    'note_table_headers': [
        'Note ID', 'Created By', 'Title', 'Description', 'Action'
    ]
}


class ManageNoteView(LoginRequiredMixin, View):
    """
    View to manage notes (placeholder methods).
    """
    login_url = settings.LOGIN_URL

    def get(self, request):
        """
        Placeholder GET method for managing notes.
        """
        pass

    def post(self, request):
        """
        Placeholder POST method for managing notes.
        """
        pass


class CreateNoteView(LoginRequiredMixin, View):
    """
    View to create notes for candidates.

    Methods:
    - get: Renders a form for creating a new note for a candidate.
    - post: Processes form data to create a new note for a candidate.
    """
    login_url = settings.LOGIN_URL

    def get(self, request, id):
        """
        GET method to render the form for creating a new note for a candidate.
        """
        form = notes_management_forms.CreateNoteForm()
        template = 'notes_management/create_candidate_note.html'
        context = {
            'form': form,
            'candidate_id': id,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)

    def post(self, request, id):
        """
        POST method to process the form data and create a new note for a candidate.
        """
        form = notes_management_forms.CreateNoteForm(request.POST)
        candidate = candidate_management_models.Candidate.objects.get(id=id)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.candidate = candidate
            note.save()
        return redirect(f'/candidate/{id}/')


class UpdateNoteView(LoginRequiredMixin, View):
    """
    View to update notes associated with candidates.

    Methods:
    - get: Renders a form to update a candidate's note.
    - post: Updates a candidate's note based on form data.
    """
    login_url = settings.LOGIN_URL

    def get(self, request, id):
        """
        GET method to render the form to update a candidate's note.
        """
        form = notes_management_forms.UpdateNoteForm()
        note = notes_management_models.Note.objects.get(id=id)
        template = 'notes_management/update_candidate_note.html'
        context = {
            'form': form,
            'note': note,
            'delete_candidate_note_url': f'/candidate/{note.candidate.id}/note/{note.id}/delete',
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)

    def post(self, request, id):
        """
        POST method to update a candidate's note.
        """
        form = notes_management_forms.UpdateNoteForm(request.POST)
        note = notes_management_models.Note.objects.get(id=id)
        candidate = note.candidate
        if form.is_valid():
            note.user = form.cleaned_data['user']
            note.candidate = candidate
            note.title = form.cleaned_data['title']
            note.description = form.cleaned_data['description']
            note.save()
        return redirect(f'/candidate/{candidate.id}/')


class DeleteNoteView(LoginRequiredMixin, View):
    """
    View to delete notes associated with candidates.

    Methods:
    - get: Renders the confirmation page for deleting a candidate's note.
    - post: Deletes a candidate's note.
    """
    login_url = settings.LOGIN_URL

    def get(self, request, id):
        """
        GET method to render the confirmation page for deleting a candidate's note.
        """
        template = 'notes_management/delete_candidate_note.html'
        note = notes_management_models.Note.objects.get(id=id)
        context = {
            'candidate_note_base_url': f'/candidate/{note.candidate.id}/note/{note.id}',
            'note': note,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)

    def post(self, request, id):
        """
        POST method to delete a candidate's note.
        """
        note = notes_management_models.Note.objects.get(id=id)
        note.delete()
        return redirect(f'/candidate/{note.candidate.id}/')
