from django.contrib.auth.models import User
from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'slug', 'author', 'body',
                  'publish', 'created', 'updated', 'status', ]

    def get_author(self, obj):
        return {'username': obj.author.username,
                'first_name': obj.author.first_name,
                'last_name': obj.author.last_name,
                'email': obj.author.email}

    def get_fields(self):
        fields = super().get_fields()
        if self.context.get('request').method == 'GET':
            fields.update({'author':  serializers.SerializerMethodField()})
        return fields


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = ['post', 'name', 'email', 'body',
                  'created', 'updated', 'active', ]
