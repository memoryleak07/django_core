# from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import Post

from .api.serializers import PostSerializer
from .api.pagination import SmallSetPagination
from .api.permissions import IsOwnOrAdminOrReadOnly


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = SmallSetPagination
    filter_backends = [SearchFilter]
    search_fields = ["title"]
    
    def perform_create(self, serializer):
        # Automatically set the author to the current user when creating a new Post
        serializer.save(author=self.request.user)
        


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnOrAdminOrReadOnly]
    
    def perform_update(self, serializer):
        # Automatically set the author to the current user when updating a Post
        serializer.save(author=self.request.user)    
    
