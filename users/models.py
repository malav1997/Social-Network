from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractUser):
	def __str__(self):
		return self.email

class Post(models.Model):
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	imgfile = models.ImageField(upload_to='posts/', blank=True, null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Comment(models.Model):
	comment_auth = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	title = models.ForeignKey(Post, on_delete=models.CASCADE)
	ctext = models.TextField(blank=True, null=True, max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.ctext
