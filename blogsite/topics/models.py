from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True, editable = False)
    details = models.TextField(max_length = 1024, default=' ')
    added_date = models.DateTimeField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('topics:detail', args=(self.slug,))

    class Meta:
        ordering = ['name']
