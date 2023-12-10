from django import forms
from candidate_management import models


class CreateCandidateForm(forms.ModelForm):
    class Meta:
        model = models.Candidate
        fields = ['first_name', 'last_name', 'contact_number', 'resume']


class UpdateCandidateForm(forms.ModelForm):
    class Meta:
        model = models.Candidate
        fields = ['first_name', 'last_name', 'contact_number', 'resume']
