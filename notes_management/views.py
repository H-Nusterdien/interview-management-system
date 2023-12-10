from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from notes_management import forms, models


BASE_CONTEXT = {
    'urls': {
        'sign_up': settings.SIGN_UP_URL,
        'login': settings.LOGIN_URL,
        'logout': settings.LOGOUT_URL,
    }
}


class ManageNoteView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request):
        pass

    def post(self, request):
        pass


class CreateNoteView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, id):
        form = forms.CreateNoteForm()
        template = 'notes_management/create_candidate_note.html'
        context = {
            'form': form,
            'candidate_id': id,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)

    def post(self, request):
        form = forms.CreateNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.candidate = request.candidate
            note.save()
        return redirect('/')


class UpdateNoteView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, id):
        form = forms.UpdateNoteForm()
        note = models.Note.objects.get(id=id)
        template = 'notes_management/update_candidate_note.html'

        note_table_headers = [
            'Note ID', 'Created By', 'Title', 'Description', 'Action'
        ]

        context = {
            'form': form,
            'note': note,
            'delete_candidate_note_url': f'/candidate/{note.candidate.id}/note/{note.id}/delete',
            'note_table_headers': note_table_headers,
        }

        context.update(BASE_CONTEXT)

        return render(request, template, context)

    def post(self, request):
        pass

class DeleteNoteView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request):
        pass

    def post(self, request):
        pass