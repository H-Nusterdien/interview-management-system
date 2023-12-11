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
    'candidate_table_headers': [
        'Candidate ID', 'First Name', 'Last Name', 'Contact Number', "Resume", 'Action'
    ],
    'note_table_headers': [
        'Note ID', 'Created By', 'Title', 'Description', 'Action'
    ]
}


class ManageCandidateView(LoginRequiredMixin, View):
    """
    View to manage candidate details and associated notes.

    Methods:
    - get: Retrieves and renders candidate details and associated notes.
    """
    login_url = settings.LOGIN_URL

    def get(self, request, id):
        """
        GET method to render candidate details and associated notes.
        """
        template = 'candidate_management/manage_candidate.html'
        candidate = candidate_management_models.Candidate.objects.get(id=id)
        notes = notes_management_models.Note.objects.filter(candidate__id=candidate.id)
        context = {
            'candidate': candidate,
            'candidate_base_url': f'/candidate/{id}',
            'candidate_table': {
                'table_headers': BASE_CONTEXT['candidate_table_headers'],
            },
            'candidate_note_base_url': f'/candidate/{id}/note',
            'create_candidate_note_url': f'/candidate/{id}/note/create/',
            'notes_table': {
                'table_headers': BASE_CONTEXT['note_table_headers'],
                'notes': notes,
            },
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)


class CreateCandidateView(LoginRequiredMixin, View):
    """
    View to create a new candidate.

    Methods:
    - get: Renders the form to create a new candidate.
    - post: Processes form data to create a new candidate.
    """
    login_url = settings.LOGIN_URL

    def get(self, request):
        """
        GET method to render the form for creating a new candidate.
        """
        template = 'candidate_management/create_candidate.html'
        form = candidate_management_forms.CreateCandidateForm()
        context = {
            'form': form,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)

    def post(self, request):
        """
        POST method to process form data and create a new candidate.
        """
        form = candidate_management_forms.CreateCandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return redirect('/candidate/create/')


class UpdateCandidateView(LoginRequiredMixin, View):
    """
    View to update candidate details.

    Methods:
    - get: Renders the form to update candidate details.
    - post: Processes form data to update candidate details.
    """
    login_url = settings.LOGIN_URL

    def get(self, request, id):
        """
        GET method to render the form to update candidate details.
        """
        template = 'candidate_management/update_candidate.html'
        form = candidate_management_forms.UpdateCandidateForm()
        candidate = candidate_management_models.Candidate.objects.get(id=id)
        context = {
            'form': form,
            'candidate_base_url': f'/candidate/{id}',
            'candidate': candidate,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)

    def post(self, request, id):
        """
        POST method to process form data and update candidate details.
        """
        form = candidate_management_forms.UpdateCandidateForm(request.POST)
        candidate = candidate_management_models.Candidate.objects.get(id=id)
        if form.is_valid():
            candidate.first_name = form.cleaned_data['first_name']
            candidate.last_name = form.cleaned_data['last_name']
            candidate.contact_number = form.cleaned_data['contact_number']
            candidate.resume = form.cleaned_data['resume']
            candidate.save()
        return redirect(f'/candidate/{id}/')


class DeleteCandidateView(LoginRequiredMixin, View):
    """
    View to delete a candidate.

    Methods:
    - get: Renders the confirmation page for deleting a candidate.
    - post: Processes the deletion of a candidate.
    """
    login_url = settings.LOGIN_URL

    def get(self, request, id):
        """
        GET method to render the confirmation page for deleting a candidate.
        """
        template = 'candidate_management/delete_candidate.html'
        candidate = candidate_management_models.Candidate.objects.get(id=id)
        context = {
            'candidate_base_url': f'/candidate/{id}',
            'candidate': candidate,
        }
        context.update(BASE_CONTEXT)
        return render(request, template, context)

    def post(self, request, id):
        """
        POST method to process the deletion of a candidate.
        """
        candidate = candidate_management_models.Candidate.objects.get(id=id)
        candidate.delete()
        return redirect('/')
