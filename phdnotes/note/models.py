from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.postgres.fields import ArrayField

from reference.models import Reference

class Note(models.Model):

    content = models.TextField()
    tags = ArrayField(models.CharField(max_length=32), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    reference = models.ForeignKey(Reference, related_name='notes')

    def __str__(self):
        return str(self.created_at)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk': self.pk})
