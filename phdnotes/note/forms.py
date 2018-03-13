from django import forms

from .models import Note


class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(BaseModelForm, self).__init__(*args, **kwargs)


class MyTextarea(forms.Textarea):
    template_name = 'note/my_text_area.html'

    def __init__(self, attrs=None):
        default_attrs = {'cols': '60', 'rows': '15'}
        if attrs:
            default_attrs.update(attrs)

        super().__init__(default_attrs)


class NoteForm(BaseModelForm):
    content = forms.CharField(widget=MyTextarea())

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
