from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    pub_date = models.DateTimeField(verbose_name='date published', auto_now_add=True)

    def __str__(self):
        return self.title
