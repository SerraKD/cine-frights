from django.db import models
from cloudinary.models import CloudinaryField


class Member(models.Model):
    """
    Class for newsletter subscription
    """
    email = models.EmailField(unique=True)
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    """
    Class for newsletter
    """
    subject = models.CharField(max_length=200, unique=True, default="subject")
    contents = models.TextField(blank=False, null=False, default="text")
    images = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.subject
