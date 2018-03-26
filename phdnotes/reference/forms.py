from django.forms import ModelForm
from .models import Reference


class ReferenceForm(ModelForm):

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
