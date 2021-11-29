from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_1 = SimpleRouter()

router_1.register(r'posts', PostViewSet, basename='post')
router_1.register(r'groups', GroupViewSet, basename='group')
router_1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment_list'
)
router_1.register(
    r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router_1.urls)),
]
