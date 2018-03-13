from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.postgres.fields import ArrayField


class Reference(models.Model):

    abstract = models.TextField()
    ref = models.CharField(max_length=128)
    authors = ArrayField(models.CharField(max_length=32))
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    source = models.URLField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk': self.pk})
