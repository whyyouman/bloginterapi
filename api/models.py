from django.db import models

# Create your models here.

class Blog(models.Model):
	image = models.CharField(max_length=20, default='')
	title = models.CharField(max_length=20, default='')
	content = models.TextField(default='')
	date = models.CharField(max_length=20, default='')
