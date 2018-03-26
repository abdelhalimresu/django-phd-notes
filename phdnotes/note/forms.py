from ckeditor.fields import RichTextFormField
from django.forms import ModelForm
from .models import Note


class NoteForm(ModelForm):

    content = RichTextFormField()

    class Meta:
        model = Note
        fields = [
            'content',
            'tags',
            'reference',
        ]
        help_texts = {
            'tags': 'Separate tags with ","',
        }
