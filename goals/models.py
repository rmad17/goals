from django.db import models
from django.contrib.auth.models import User
import uuid


class Goal(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='goals')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    target_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = "Life Goal"

    def __str__(self):
        return self.title
