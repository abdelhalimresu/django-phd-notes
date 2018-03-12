from django.conf.urls import url
from note.views import NoteCreateView
from note.views import NoteDetailView
from note.views import NoteListView
from note.views import NoteUpdateView

urlpatterns = [
    url(r'^create/$', NoteCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', NoteUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/$', NoteDetailView.as_view(), name='detail'),
    url(r'$', NoteListView.as_view(), name='list'),
]
