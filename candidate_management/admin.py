from django.contrib import admin
from candidate_management.models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Candidate)
