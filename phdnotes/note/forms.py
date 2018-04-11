from ckeditor.fields import RichTextFormField
from django.forms import ModelForm
from .models import Note
from .models import Comment


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


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = [
            'text',
            'note',
        ]
