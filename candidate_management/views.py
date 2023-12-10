from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

from candidate_management import models as candidate_management_models
from candidate_management import forms as candidate_management_forms

from notes_management import models as notes_management_models


BASE_CONTEXT = {
    'urls': {
        'sign_up': settings.SIGN_UP_URL,
        'login': settings.LOGIN_URL,
        'logout': settings.LOGOUT_URL,
    },
    'candidate_table_headers' : [
        'Candidate ID', 'First Name', 'Last Name', 'Contact Number', "Resume", 'Action'
    ],
    'notes_table_headers' : [
        'Note ID', 'Title', 'Description', 'Action'
    ]
}


class ManageCandidateView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, id):
        template = 'candidate_management/manage_candidate.html'

        candidate = candidate_management_models.Candidate.objects.get(id=id)
        notes = notes_management_models.Note.objects.filter(id=candidate.id)

        context = {
            'candidate': candidate,
            
            # Candidate Management
            'candidate_base_url': f'/candidate/{id}',
            'candidate_table': {
                'table_headers': BASE_CONTEXT['candidate_table_headers'],
            },

            # Notes Management
            'candidate_note_base_url': f'/candidate/{id}/note',
            'create_candidate_note_url': f'/candidate/{id}/note/create/',
            'notes_table': {
                'table_headers': BASE_CONTEXT['notes_table_headers'],
                'notes': notes,
            },
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)

    def post(self, request, id=id):
        pass


class CreateCandidateView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    
    def get(self, request):
        template = 'candidate_management/create_candidate.html'
        form = candidate_management_forms.CreateCandidateForm
        context = {
            'form': form,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)

    def post(self, request):
        pass


class UpdateCandidateView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    
    def get(self, request, id):
        template = 'candidate_management/update_candidate.html'
        form = candidate_management_forms.UpdateCandidateForm
        candidate = candidate_management_models.Candidate.objects.get(id=id)
       
        context = {
            'form': form,
            'candidate_base_url': f'/candidate/{id}',
            'candidate': candidate,
        }

        context.update(BASE_CONTEXT)

        return render(request, template, context)

    def post(self, request):
        pass


class DeleteCandidateView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    
    def get(self, request, id=id):
        pass

    def post(self, request):
        pass
