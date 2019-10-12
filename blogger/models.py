from django.db import models
import os

# media_location = './media/{}'.format(os.mkdir(title))

# class BlogPost(models.Model):
# 	title = models.CharField(max_length=128)
# 	topic = models.CharField(max_length=50)
# 	description = models.CharField(max_length=140)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	writer = models.ForeignKey('Blogger', on_delete=models.CASCADE)
# 	content = models.TextField()
# 	blog_images = models.ImageField(upload_to=media_location)

# 	def __str__(self):
# 		return self.title, self.topic, self.created_at


# class Blogger(models.Model):
# 	firstName = models.CharField(max_length=50)
# 	lastName = models.CharField(max_length=50)
# 	email = models.EmailField(max_length=254, unique=True)
