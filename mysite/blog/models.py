from django.db import models
from django.utils import timezone

PRIORITY_CHOICES = (('Python', 'Python'),
                    ('Django', 'Django'),
                    ('GitHub', 'GitHub'))


class post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default='Python')
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

