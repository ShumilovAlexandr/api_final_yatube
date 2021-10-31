from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer,
                          GroupSerializer, PostSerializer)
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post, User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs["id"])
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.GenericViewSet, CreateModelMixin, ListModelMixin):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthorOrReadOnly]
