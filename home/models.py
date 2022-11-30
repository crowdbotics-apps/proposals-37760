from django.conf import settings
from django.db import models
class Project(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
    client = models.ForeignKey("home.Client",on_delete=models.CASCADE,null=True,blank=True,related_name="project_client",)
class Client(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
