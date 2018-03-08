from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView

from .models import Note
from .forms import NoteForm


class HomeView(View):
    model = Note


class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note


class NoteCreateView(CreateView):
    form_class = NoteForm
    model = Note


class NoteUpdateView(UpdateView):
    form_class = NoteForm
    model = Note
