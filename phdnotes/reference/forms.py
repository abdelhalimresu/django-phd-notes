from django import forms

from .models import Reference


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


class ReferenceForm(BaseModelForm):
    abstract = forms.CharField(strip=False, widget=MyTextarea())

    class Meta:
        model = Reference
        fields = [
            'name',
            'abstract',
            'authors',
            'ref',
            'source',
        ]
        help_texts = {
            'authors': 'Separate authors with ","',
        }
