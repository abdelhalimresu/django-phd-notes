from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.postgres.fields import ArrayField


class Note(models.Model):

    content = models.TextField()
    tags = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk': self.pk})
