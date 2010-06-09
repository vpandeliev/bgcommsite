from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=80)
	author = models.CharField()
	date = models.DateField()
    text = models.CharField()
