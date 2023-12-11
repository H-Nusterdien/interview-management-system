from django import forms
from candidate_management import models


class CreateCandidateForm(forms.ModelForm):
    """
    Form for creating a new candidate.

    Uses Django's ModelForm to create a form based on the Candidate model.

    Fields:
    - first_name: CharField for the candidate's first name.
    - last_name: CharField for the candidate's last name.
    - contact_number: CharField for the candidate's contact number.
    - resume: FileField for the candidate's resume (optional).
    """
    class Meta:
        model = models.Candidate
        fields = ['first_name', 'last_name', 'contact_number', 'resume']


class UpdateCandidateForm(forms.ModelForm):
    """
    Form for updating an existing candidate.

    Uses Django's ModelForm to create a form based on the Candidate model.

    Fields:
    - first_name: CharField for the candidate's first name.
    - last_name: CharField for the candidate's last name.
    - contact_number: CharField for the candidate's contact number.
    - resume: FileField for the candidate's resume (optional).
    """
    class Meta:
        model = models.Candidate
        fields = ['first_name', 'last_name', 'contact_number', 'resume']
