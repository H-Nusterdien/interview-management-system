from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from notes_management import forms as notes_management_forms
from notes_management import models as notes_management_models

from candidate_management import models as candidate_management_models


BASE_CONTEXT = {
    'urls': {
        'sign_up': settings.SIGN_UP_URL,
        'login': settings.LOGIN_URL,
        'logout': settings.LOGOUT_URL,
    },
    'note_table_headers' : [
        'Note ID', 'Created By', 'Title', 'Description', 'Action'
    ]
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
        form = notes_management_forms.CreateNoteForm()
        template = 'notes_management/create_candidate_note.html'
        context = {
            'form': form,
            'candidate_id': id,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)

    def post(self, request, id):
        form = notes_management_forms.CreateNoteForm(request.POST)
        candidate = candidate_management_models.Candidate.objects.get(id=id)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.candidate = candidate
            note.save()
        return redirect(f'/candidate/{id}/')


class UpdateNoteView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, id):
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
    login_url = settings.LOGIN_URL

    def get(self, request, id):
        template = 'notes_management/delete_candidate_note.html'
        note = notes_management_models.Note.objects.get(id=id)
        context = {
            'candidate_note_base_url': f'/candidate/{note.candidate.id}/note/{note.id}',
            'note': note,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)

    def post(self, request, id):
        note = notes_management_models.Note.objects.get(id=id)
        note.delete()
        return redirect(f'/candidate/{note.candidate.id}/')
