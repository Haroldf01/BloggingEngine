from rest_framework import serializers
from . import models


class BloggerSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=254)
    topic = serializers.CharField(max_length=50)
    description = serializers.CharField()
    content = serializers.CharField()
    img = serializers.ImageField(
        allow_empty_file=True, required=False, use_url=True)

    def create(self, validated_data):
        return models.Blogger.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print('\n', '\n', 'Inside Update Method', '\n', '\n', )
        print('\nValidated Data', instance.description, '\n')
        print(type(validated_data))
        instance.title = validated_data.get('title', instance.title)
        instance.topic = validated_data.get('topic', instance.topic)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.content = validated_data.get('content', instance.content)
        instance.img = validated_data.get('img', instance.img)
        instance.author = validated_data.get('author', instance.author)

        print('\ninstance Validation COMPLETED' '\n')

        instance.save()
        return instance
