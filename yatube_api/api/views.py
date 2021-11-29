from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post

CREATE_DENIED_MESSAGE = 'Необходима авторизация для создания поста'
DELETE = 'Удаление чужого контента запрещено'
UPDATE = 'Изменение чужого контента запрещено!'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied(CREATE_DENIED_MESSAGE)
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied(UPDATE)
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(DELETE)
        instance.delete()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied(UPDATE)
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(
                DELETE)
        instance.delete()

    def get_queryset(self):
        # получаем список всех комментариев поста с
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, serializer):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
