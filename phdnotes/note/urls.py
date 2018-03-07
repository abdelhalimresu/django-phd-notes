from django.conf.urls import url


from .views import NoteListView

urlpatterns = [
    url(r'$', NoteListView.as_view(), name='list'),
]
