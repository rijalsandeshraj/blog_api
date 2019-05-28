from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer


class PostListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'


class ListViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "title"
    pagination_class = PostListPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering_fields = ('publish',)
    search_fields = ('title', 'body')

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
