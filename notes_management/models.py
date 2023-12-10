from django.db import models
from django.contrib.auth.models import User
from candidate_management import models as candidate_management_models


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(candidate_management_models.Candidate, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title + "\n" + self.description
    
    def create_note(self):
        pass

    def update_note(self):
        pass

    def delete_note(self):
        pass

    def get_note(self):
        pass

