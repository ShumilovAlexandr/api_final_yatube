from django.urls import include, path
from rest_framework import routers

from .views import (CommentViewSet, FollowViewSet, GroupViewSet,
                    PostViewSet)

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register('follow', FollowViewSet, basename='following')
router.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]