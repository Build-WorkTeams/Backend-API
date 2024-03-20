from django.db import models
from django.conf import settings

from .utils import upload_filename

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks',
                             on_delete=models.CASCADE)

    def __str__(self):
        return f"Task: {self.title}"
    

class Step(models.Model):
    note = models.CharField(max_length=200)
    attachment = models.FileField(upload_to=upload_filename, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, related_name='steps',
                             on_delete=models.CASCADE)

    def __str__(self):
        return f"Step: {self.note}"