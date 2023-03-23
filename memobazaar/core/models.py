from django.db import models
from django.contrib.auth.models import User

class Memo(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
