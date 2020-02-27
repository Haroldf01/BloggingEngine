from django.db import models
from django.conf import settings
from user.models import User

from django.template.defaultfilters import slugify

STATUS = (
	(0, 'draft'),
	(1, 'publish')
)

class Category(models.Model):
	name = models.CharField(max_length=254)
	slug = models.SlugField()
	parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('slug', 'parent')
		verbose_name_plural = 'categories'

	def __str__(self):
		full_path = [self.name]
		k = self.parent
		while k is not None:
			full_path.append(k.name)
			k = k.parent
		return ' -> '.join(full_path[::-1])


class Blogger(models.Model):
	title = models.CharField(max_length=254, unique=True)
	slug = models.SlugField(max_length=254, unique=True)
	topic = models.CharField(max_length=50)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_posts', on_delete=models.CASCADE)
	category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
	description = models.CharField(max_length=140)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	content = models.TextField()
	status = models.IntegerField(choices=STATUS, default=0)
	img = models.ImageField(upload_to=settings.MEDIA_ROOT)

	class Meta:
		ordering = ['-created_on', '-updated_on']

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Blogger, self).save(*args, **kwargs)

	def __str__(self):
		return self.title
