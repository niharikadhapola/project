from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class blog_posts(models.Model):
    Initiative_Title = models.CharField(max_length=255, unique = True)
    requirements = models.CharField(max_length=40000, default= " ")
    name = models.CharField(max_length=100)
    budget = models.PositiveIntegerField(default = 0)
    location = models.CharField(max_length=100, default = "")
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attending', blank=True)
    num_of_attendees = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.title

    def get_post_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})
