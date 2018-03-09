from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Note
from .forms import NoteForm


class HomeView(View):
    model = Note


class NoteListView(ListView):

    def get_queryset(self):
        tag = self.request.GET.get("tags")

        if tag:
            return Note.objects.filter(tags__contains=[tag])

        return Note.objects.all()


class NoteDetailView(DetailView):
    model = Note


class NoteCreateView(CreateView):
    form_class = NoteForm
    model = Note
    success_url = reverse_lazy('notes:list')


class NoteUpdateView(UpdateView):
    form_class = NoteForm
    model = Note
    success_url = reverse_lazy('notes:list')
