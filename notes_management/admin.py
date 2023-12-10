from django.contrib import admin
from notes_management import models


class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Note)
