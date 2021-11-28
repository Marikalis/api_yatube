from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()

router.register(r'api/v1/posts', PostViewSet)
router.register(r'api/v1/groups', GroupViewSet)
router.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='post_id'
)
router.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/',
    CommentViewSet,
    basename='comment_id'
)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
