from django.db import models


class Candidate(models.Model):
    """
    Model to represent candidates.

    Fields:
    - first_name: CharField for candidate's first name.
    - last_name: CharField for candidate's last name.
    - contact_number: CharField for candidate's contact number.
    - resume: FileField to store candidate's resume (optional).
    - created_at: DateTimeField indicating the creation timestamp of the candidate.
    - updated_at: DateTimeField indicating the last update timestamp of the candidate.

    Methods:
    - __str__: Returns a string representation of the Candidate object.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)
    resume = models.FileField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        String representation of a Candidate object.
        """
        return f"{self.first_name} {self.last_name}"
