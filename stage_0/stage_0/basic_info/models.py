from django.db import models

# Create your models here.
class MyModel(models.Model):
    email = models.EmailField()
    current_datetime = models.DateTimeField(auto_now_add=True)
    github_url = models.URLField()
