from django.shortcuts import render
from django.views.generic import View, ListView

from .models import Note


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "base.html")


class NoteListView(ListView):
    def get_queryset(self):
        return Note.objects.all()
