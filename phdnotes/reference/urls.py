from django.conf.urls import url
from .views import ReferenceCreateView
from .views import ReferenceDetailView
from .views import ReferenceListView
from .views import ReferenceUpdateView

urlpatterns = [
    url(r'^create/$', ReferenceCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', ReferenceUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/$', ReferenceDetailView.as_view(), name='detail'),
    url(r'$', ReferenceListView.as_view(), name='list'),
]
