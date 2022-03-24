# Create your models here.
from django.db import models

from django.conf import settings


class Post(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.TextField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    body = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True, null=False)
    updated_dt = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    post = models.ForeignKey(Post, null=False, blank=False,related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    created_dt = models.DateField(auto_now_add=True, null=False, blank=False)
    comment = models.TextField()

    def __str__(self):
        return self.comment