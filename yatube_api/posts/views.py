from api.permissions import IsAuthorOrReadOnly
from api.serializers import (CommentSerializer, FollowCreateSerializer,
                             FollowListSerializer, GroupSerializer,
                             PostSerializer)
from rest_framework import mixins, permissions, viewsets, filters
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination

from .models import Comment, Follow, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs["id"])
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):

    permission_class = (permissions.IsAuthenticated, )
    queryset = Follow.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('user__username', 'following__username')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FollowListSerializer
        return FollowCreateSerializer

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthorOrReadOnly]
