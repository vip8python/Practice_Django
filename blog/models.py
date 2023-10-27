from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255, help_text='0-255 symbol', db_index=True)
    content = models.TextField(max_length=5000, blank=True, null=True, help_text='0-5000 symbol')
    date_created = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'create post'
        verbose_name_plural = 'create posts'

    def __str__(self):
        return self.title