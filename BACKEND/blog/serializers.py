from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'slug', 'author',
                  'publish', 'created', 'updated', 'status', ]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = ['post', 'name', 'email', 'body',
                  'created', 'updated', 'active', ]
