from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=250)
    project = models.CharField(max_length=250)
    done = models.BooleanField(default=False)
