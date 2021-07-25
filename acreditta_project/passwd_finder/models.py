from django.db import models

# Create your models here.
class PasswdFinder(models.Model):
    passwd = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)