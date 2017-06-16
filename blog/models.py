from django.contrib.auth.models import User
from django.db import models

short_text_lengh = 1000

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > short_text_lengh:
            return self.text[:short_text_lengh]
        else:
            return self.text