from django.db import models
from django.conf import settings
from user.models import User
import os


STATUS = (
	(0, 'draft'),
	(1, 'publish')
)

class Blogger(models.Model):
	title = models.CharField(max_length=254, unique=True)
	slug = models.SlugField(max_length=254, unique=True)
	topic = models.CharField(max_length=50)
	auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
	description = models.CharField(max_length=140)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	content = models.TextField()
	status = models.IntegerField(choices=STATUS, default=0)
	img = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT))

	class Meta:
		ordering = ['-created_on', '-updated_on']

	def __str__(self):
		return self.title
