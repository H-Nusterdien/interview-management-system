from django.db import models
from django.contrib.auth.models import User
from candidate_management import models as candidate_management_models


class Note(models.Model):
    """
    Model to represent notes associated with candidates.

    Fields:
    - user: ForeignKey to User model representing the user who created the note.
    - candidate: ForeignKey to Candidate model representing the associated candidate.
    - title: CharField for the title of the note.
    - description: TextField for the description/content of the note.
    - created_at: DateTimeField indicating the creation timestamp of the note.
    - updated_at: DateTimeField indicating the last update timestamp of the note.

    Methods:
    - __str__: Returns a string representation of the Note object displaying its title and description.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(candidate_management_models.Candidate, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        String representation of a Note object.
        """
        return f'Title: {self.title} | Description: {self.description}'
