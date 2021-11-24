from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets 

from posts.models import Comment, Group, Post
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # получаем список всех комментариев поста с
        id = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post=id)
        return new_queryset


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#    if request.method == 'GET':
#        serializer = PostSerializer(post)
#        return Response(serializer.data)
#
#   user = request.user
#   
#   if user != post.author:
#       return Response(status=status.HTTP_403_FORBIDDEN)
