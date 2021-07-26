from django.db import models

# Create your models here.
class Tasks(models.Model):
    task=models.CharField(max_length=255)
    is_complete=models.BooleanField(default=False)
    time=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-time',)

    def __str__(self):
        return self.task