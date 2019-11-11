from rest_framework import serializers
from . import models

class BloggerSerializer(serializers.ModelSerializer):

	class Meta:
		fields = '__all__'
		model = models.Blogger
