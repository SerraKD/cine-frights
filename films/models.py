from django.db import models

class NewsLetter(models.Model):
    '''Class for newsletter subscription '''
    email = models.EmailField(unique=True)
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.email 