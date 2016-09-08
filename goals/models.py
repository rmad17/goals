from django.db import models
from django.contrib.auth.models import User
import uuid


class Goal(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    target_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        ordering = ('created_at',)
        verbose_name = "Life Goal"

    def as_dict(self):
        return {'uuid': self.uuid, 'title': self.title, 'target_date':
                self.target_date, 'end_date': self.end_date}

    def __str__(self):
        return self.title
