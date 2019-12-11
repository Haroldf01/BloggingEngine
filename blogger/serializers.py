from rest_framework import serializers
from . import models


class BloggerSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=254)
	topic = serializers.CharField(max_length=50)
	description = serializers.CharField()
	content = serializers.CharField()
	img = serializers.ImageField(allow_empty_file=True, required=False, use_url=True)
	author = serializers.CharField()

	def create(self, validated_data):
		print('\n', validated_data, '\n')
		return models.Blogger.objects.create(**validated_data)

	def update(self, instance, validated_data):
		print('\n', '\n', 'Inside Update Method', '\n', '\n', )
		instance.title = validated_data('title', instance.title)
		instance.topic = validated_data('topic', instance.topic)
		instance.description = validated_data('description', instance.description)
		instance.content = validated_data('content', instance.content)
		instance.author = validated_data('author', instance.author)

		instance.save()
		return instance
