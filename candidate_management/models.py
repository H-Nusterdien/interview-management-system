from django.db import models
from django.urls import reverse


class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)
    resume = models.FileField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def create_candidate(self):
        pass

    def update_candidate(self):
        pass

    def delete_candidate(self):
        pass

    def get_absolute_url(self) -> str:
        return reverse("manage_candidate", kwargs={"id": self.id})
