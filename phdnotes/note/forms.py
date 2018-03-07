from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]
