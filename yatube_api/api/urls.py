from django.urls import include, path
from posts.views import (CommentViewSet, FollowViewSet, GroupViewSet,
                         PostViewSet)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register(r'follow', FollowViewSet, basename='following')
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]
