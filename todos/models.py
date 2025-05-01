from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Alterado para DateTimeField
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateField(null=True, blank=True)  # Adicionado blank=True

    def __str__(self):
        return self.title